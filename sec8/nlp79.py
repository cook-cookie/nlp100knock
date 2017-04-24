import pickle
from collections import Counter
import numpy as np
from nlp76 import prediction_enhanced
from nlp77 import calc_scores
from nlp78 import check_pred

if __name__ == '__main__':
    N = 10662

    s = pickle.load(open('nlp73_pickle', 'rb'))

    with open('features_mod.txt') as f:
        fi = f.readlines()

    score_list = []
    for border in np.arange(0, 1.1, 0.1):
        pred_list = []
        for sentence in fi:
            pred_list.append(check_pred(prediction_enhanced(sentence, s, border)))
        print('正解率, 適合率, 再現率, F1スコア')
        score_list.append(calc_scores(Counter(pred_list), N))
        print(*calc_scores(Counter(pred_list), N), sep='\t')
        print('----------------------------------------')
