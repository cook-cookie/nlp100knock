import pickle
from collections import Counter
import numpy as np
from nlp76 import prediction_enhanced
from nlp77 import calc_scores
from nlp78 import check_pred
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

if __name__ == '__main__':
    N = 10662

    s = pickle.load(open('nlp73_pickle', 'rb'))

    plt.style.use('ggplot')
    font = {'family': 'meiryo'}
    matplotlib.rc('font', **font)

    with open('features_mod.txt') as f:
        fi = f.readlines()

    recall_list = []
    precision_list = []
    for border in np.arange(0, 1.0, 0.1):
        pred_list = []
        for sentence in fi:
            pred_list.append(check_pred(prediction_enhanced(sentence, s, border)))
        print(border, '正解率, 適合率, 再現率, F1スコア')
        score = calc_scores(Counter(pred_list), N)
        recall_list.append(score[2])
        precision_list.append(score[1])
        print(np.round(calc_scores(Counter(pred_list), N), 3), sep='\t')
        print('----------------------------------------')
    # print(*recall_list, sep=', ')
    # print(*precision_list, sep=', ')
    # print(len(recall_list), len(precision_list))
    plt.plot(recall_list, precision_list)
    plt.show()
