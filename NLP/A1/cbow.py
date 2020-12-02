import json
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
# settings = {
#     'epochs': 10,
#     'window_size': 5,
#     'learning_rate': 0.01,
#     'n': 10
# }

# class cbow():
#     def __init__(self):
#         self.epochs = settings['epochs']
#         self.window_size = settings['window_size']
#         self.learning_rate = settings['learning_rate']
#         self.n = settings['n']

def get_data(stop_word_removal='no'):
    fileIn = open('data.json', 'r')
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

corpus = get_data('yes')
print(corpus)
