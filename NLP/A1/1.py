import numpy as np
import re
import json
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import np_utils

stop_words = set(stopwords.words('english'))

settings = {
    'learningRate': 0.01,
    'n': 2,
    'window_size': 2,
    'epochs': 1,
}


def softmax(v):
    eVal = np.exp(v-np.max(v))
    return eVal/eVal.sum(axis=0)



def tokenize(corpus):
    tokenize = Tokenizer()
    tokenize.fit_on_texts(corpus)

    return tokenize.texts_to_sequences(corpus), len(tokenize.word_index)



def cbow(ctxtV, label, w1, w2, loss):
    muMat = np.mean(ctxtV, axis=0)
    hMat = np.dot(w1.T, muMat)
    uMat = np.dot(w2.T, hMat)

    y_pred = softmax(uMat)

    L = -label+y_pred
    
    dL_w2 = np.outer(hMat, L)
    dL_w1 = np.outer(muMat, np.dot(dL_w2, L))

    loss += -float(uMat[label == 1]) + np.log(np.sum(np.exp(uMat)))
    new_w2 = w2 - settings['learningRate'] * dL_w2
    new_w1 = w1 - settings['learningRate'] * dL_w1

    return new_w1, new_w2, loss






def to_categorical(y, num_classes=None):
    y = np.array(y, dtype='int')
    input_shape = y.shape

    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])
    
    y = y.ravel()
    if not num_classes:
        num_classes = np.max(y) + 1
    
    n = y.shape[0]
    categorical = np.zeros((n, num_classes))
    categorical[np.arrange(n), y] = 1
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    
    return categorical


def corpus2contextcenter(corpusTok, V, window_size=2):
    for elements in corpusTok:
        w_len = len(elements)
        for i, word in enumerate(elements):
            
            context_words = []
            labels = []

            labels.append(word-1)

            for j in range(i-window_size, i+window_size+1):
                if j!=i and 0<=j<w_len:
                    context_words.append([elements[j]-1])

            x = np_utils.to_categorical(context_words, V)
            y = np_utils.to_categorical(context_words, V)

            yield(x, y.ravel())

def get_data(stop_word_removal='no'):
    fileIn = open('reviews_Electronics_5.json', 'r')
    data = json.load(fileIn)

    corpus = []
    for entry in data:
        for val in entry['reviewText'].split('.'):
            sent = re.findall("[A-Za-z]+", val)
            line = ''
            for words in sent:
                if stop_word_removal == 'yes':
                    if len(words) > 1 and words not in stop_words:
                        line = line + ' ' + words
                    else:
                        if len(words) > 1:
                            line = line + ' ' + words
            
            if line != '':
                corpus.append(line)
    
    return corpus

def main():
    corpusList = get_data('yes')
