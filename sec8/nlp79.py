import pickle
import numpy as np
from nlp76 import prediction_enhanced

if __name__ == '__main__':
    s = pickle.load(open('nlp73_pickle', 'rb'))

    with open('features_mod.txt') as f:
        fi = f.readlines()

    for border in np.arange(0, 1.1, 0.1):
        for sentence in fi:
            print(*prediction_enhanced(sentence, s, border), sep='\t')
