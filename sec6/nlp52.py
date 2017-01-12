from nltk import stem
from nlp50 import separate_by_sentence
from nlp51 import separate_by_space
import re

if __name__ == '__main__':
    stemmer = stem.PorterStemmer()
    for sentence in separate_by_sentence():
        for word in separate_by_space(sentence):
            word_mod = re.sub(r'[^a-z]', '', word.lower())
            print(word + '\t' + stemmer.stem(word_mod))
