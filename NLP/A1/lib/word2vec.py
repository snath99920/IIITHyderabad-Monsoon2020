import numpy as np
# from .utils import *


from keras.utils import np_utils
from keras.preprocessing.text import Tokenizer
import numpy as np


def tokenize(corpus):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(corpus)
    corpus_tokenized = tokenizer.texts_to_sequences(corpus)
    V = len(tokenizer.word_index)
    return corpus_tokenized, V


def initialize(V, N):
    np.random.seed(100)
    W1 = np.random.rand(V, N)
    W2 = np.random.rand(N, V)

    return W1, W2


def corpus2io(corpus_tokenized, V, window_size):
    """Converts corpus text into context and center words
    # Arguments
        corpus_tokenized: corpus text
        window_size: size of context window
    # Returns
        context and center words (arrays)
    """
    for words in corpus_tokenized:
        L = len(words)
        for index, word in enumerate(words):
            contexts = []
            center = []
            s = index - window_size
            e = index + window_size + 1
            contexts = contexts + [words[i]-1 for i in range(s, e) if 0 <= i < L and i != index]
            center.append(word-1)
            # x has shape c x V where c is size of contexts
            x = np_utils.to_categorical(contexts, V)
            # y has shape k x V where k is number of center words
            y = np_utils.to_categorical(center, V)
            yield (x, y)



def softmax(x):
    """Calculate softmax based probability for given input vector
    # Arguments
        x: numpy array/list
    # Returns
        softmax of input array
    """
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

class Word2Vec:
    """
    Python implementation of Word2Vec.
    # Arguments
        method : `str`
            choose method for word2vec (options: 'cbow', 'skipgram')
            [default: 'cbow']
        window_size: `integer`
            size of window [default: 1]
        n_hidden: `integer`
            size of hidden layer [default: 2]
        n_epochs: `integer`
            number of epochs [default: 1]
        learning_rate: `float` [default: 0.1]
        corpus: `str`
            corpus text
    """
    def __init__(self, method='cbow', window_size=1, n_hidden=2, n_epochs=1, corpus='', learning_rate=0.1):
        self.window = window_size
        self.N = n_hidden
        self.n_epochs = n_epochs
        self.corpus = [corpus]
        self.eta = learning_rate
        if method == 'cbow':
            self.method = self.cbow
        elif method == 'skipgram':
            self.method = self.skipgram
        else:
            raise ValueError("Method not recognized. Aborting.")

    def cbow(self, context, label, W1, W2, loss):
        """
        Implementation of Continuous-Bag-of-Words Word2Vec model
        :param context: all the context words (these represent the inputs)
        :param label: the center word (this represents the label)
        :param W1: weights from the input to the hidden layer
        :param W2: weights from the hidden to the output layer
        :param loss: float that represents the current value of the loss function
        :return: updated weights and loss
        """
        # context is 'x' from tokenizer, it is a c x V matrix
        # label is 'y' from tokenizer, it is a 1 x V matrix
        
        x = np.matrix(np.mean(context, axis=0))
        
        # x is a 1 x V matrix
        # W1 is a VxN matrix
        # h is a N x 1 matrix
        h = np.matmul(W1.T, x.T)
        
        # u is a V x 1 matrix
        u = np.matmul(W2.T, h)
        
        # W2 is an N x V matrix
        # y_pred is a V x 1 matrix
        y_pred = softmax(u)
        # e is a V x 1 matrix
        e = -label.T + y_pred
        # h is N x 1 and e is V x 1 so dW2 is N x V
        dW2 = np.outer(h, e)
        # x.T is a V x 1 matrix, W2e is a Nx1 so dW1 this is V x N
        dW1 = np.outer(x.T, np.matmul(W2, e))

        new_W1 = W1 - self.eta * dW1
        new_W2 = W2 - self.eta * dW2

        # label is a 1xV matrix so label.T is a Vx1 matrix
        loss += -float(u[label.T == 1]) + np.log(np.sum(np.exp(u)))

        return new_W1, new_W2, loss

    def skipgram(self, context, x, W1, W2, loss):
        """
        Implementation of Skip-Gram Word2Vec model
        :param context: all the context words (these represent the labels)
        :param x: the center word (this represents the input)
        :param W1: weights from the input to the hidden layer
        :param W2: weights from the hidden to the output layer
        :param loss: float that represents the current value of the loss function
        :return: updated weights and loss
        """
        # context is "x" from tokenizer, it is a c x V matrix
        # "x" is "y" from tokenizer, it is a 1 x V matrix
        # W1 has dimension V x N (N= number of features, V = vocab size)
        # x has dimension V x 1
        h = np.matmul(W1.T, x.T)
        # h has dimension N x 1
        # W2 has dimension N x V
        # u has dimension V x 1
        u = np.dot(W2.T, h)
        # y_pred has dimension V x 1
        y_pred = softmax(u)

        # context is a c by V matrix
        # e is a V x c matrix
        e = np.outer(y_pred,np.array([1]*context.shape[0]))-context.T

        # np.sum(e, axis=1) is a V x 1 vectors
        # h is an N x 1 Vector
        # dW2 is a N x V matrix
        dW2 = np.outer(h, np.sum(e, axis=1))
        # x is a V x 1 matrix
        # np.dot(W2, np.sum(e,axis=1)) is a product (N x V) (Vx 1) is Nx1
        # dW1 is an V x N matrix
        dW1 = np.outer(x, np.dot(W2, np.sum(e, axis=1)))

        new_W1 = W1 - self.eta * dW1
        new_W2 = W2 - self.eta * dW2

        loss += - np.sum([u[label.T == 1] for label in context]) + len(context) * np.log(np.sum(np.exp(u)))

        return new_W1, new_W2, loss

    def predict(self, x, W1, W2):
        """Predict output from input data and weights
        :param x: input data
        :param W1: weights from input to hidden layer
        :param W2: weights from hidden layer to output layer
        :return: output of neural network
        """
        h = np.mean([np.matmul(W1.T, xx) for xx in x], axis=0)
        u = np.dot(W2.T, h)
        return softmax(u)

    def run(self):
        """
        Main method of the Word2Vec class.
        :return: the final values of the weights W1, W2 and a history of the value of the loss function vs. epoch
        """
        if len(self.corpus) == 0:
            raise ValueError('You need to specify a corpus of text.')

        corpus_tokenized, V = tokenize(self.corpus)
        W1, W2 = initialize(V, self.N)

        loss_vs_epoch = []
        for e in range(self.n_epochs):
            loss = 0.
            for context, center in corpus2io(corpus_tokenized, V, self.window):
                W1, W2, loss = self.method(context, center, W1, W2, loss)
            loss_vs_epoch.append(loss)

        return W1, W2, loss_vs_epoch

def main():
    corpus = "I like playing football with my friends"
    cbow = Word2Vec(method="cbow", corpus=corpus,
                    window_size=1, n_hidden=2,
                    n_epochs=10, learning_rate=0.8)

    W1, W2, loss_vs_epoch = cbow.run()

    print(W1)
    #[[ 0.99870389  0.20697257]
    # [-1.01911559  2.26364436]
    # [-0.69737232  0.14131477]
    # [ 3.28315183  1.13801973]
    # [-1.42944927 -0.62142097]
    # [ 0.65359329 -2.21415048]
    # [-0.22343751 -1.17927987]]

    print(W2)
    #[[-0.97080793  1.21120331  2.15603796 -1.79083151  3.38445043 -1.65295511
    #   1.36685097]
    # [2.77323464  0.78710269  2.74152617  0.08953005  0.04400675 -1.34149651
    #   -2.19375528]]

    print(loss_vs_epoch)
    #[14.328868654443703, 12.290456644464603, 10.366644621637064,
    # 9.1759777684446622, 8.4233626997233895, 7.3952948684910256,
    # 6.1727393307549736, 5.1639476117698191, 4.6333377088153043,
    # 4.2944697259465485]

main()