import pickle

import math


def prediction_enhanced(sentence: str, s: dict) -> tuple:
    temp_list = sentence.split()
    temp_num = 0
    for word in temp_list[1:]:
        temp_num += s[word]
    g = (1. / (1. + math.exp(-temp_num)))

    return '+1' if temp_list[0] == '1' else '-1', '+1' if g >= 0.5 else '-1', g


if __name__ == '__main__':
    s = pickle.load(open('nlp73_pickle', 'rb'))

    with open('features_mod.txt') as f:
        fi = f.readlines()

    for sentence in fi:
        print(*prediction_enhanced(sentence, s), sep='\t')
