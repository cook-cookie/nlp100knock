from nltk import stem
from nlp50 import separate_by_sentence
import re

def add_stem(sentence):
    words = sentence.split()
    for word in words:
        word_mod = re.sub(r'!', '', word)
        yield word_mod + '\t' + stemmer.stem(word_mod)


if __name__ == '__main__':
    stemmer = stem.PorterStemmer()
    for sentence in separate_by_sentence():
        for word in add_stem(sentence):
            print(word)
        print('')
