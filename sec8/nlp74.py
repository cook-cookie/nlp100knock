import pickle
import math


def prediction(list_of_features: list, num_of_sentence: int) -> tuple:
    temp_list = list_of_features[num_of_sentence].split()
    temp_num = 0
    for word in temp_list[1:]:
        temp_num += s[word]
    g = (1. / (1. + math.exp(-temp_num)))

    return '+1' if temp_list[0] == '1' else '-1', g

if __name__ == '__main__':
    s = pickle.load(open('nlp73_pickle', 'rb'))

    with open('features_mod.txt') as f:
        fi = f.readlines()

    print(prediction(fi, 1))
