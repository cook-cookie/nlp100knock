from nlp73 import train, update
from nlp76 import prediction_enhanced
from nlp77 import calc_scores
from collections import Counter

N = 10662  # sentiment.txtの行数
C = 5  # N分割交差検定に用いる分割数
eta0 = 0.1  # 学習率
epoch = 10  # train()を動かす回数


def check_pred(tuple_label: tuple) -> str:  # ネガポジ判定用関数
    if tuple_label[1] == '+1':
        return 'TP' if tuple_label[0] == '+1' else 'FP'
    else:
        return 'FN' if tuple_label[0] == '+1' else 'TN'


if __name__ == '__main__':
    with open('features_mod.txt') as f:
        fi = f.readlines()
        assert type(fi) == list, 'this object has {} type.'.format(type(fi))

    testlist = []  # 検証用分割済み文章リスト:[[1つめ], [2つめ], [3つめ], [4つめ], [5つめ]]
    for i in range(C):
        split_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
        assert type(split_list) == list, 'this object has {} type.'.format(type(split_list))
        testlist.append(split_list)
    assert type(testlist) == list, 'this object has {} type.'.format(type(testlist))

    score_list = []
    for i in range(C):
        # 学習用データの作成
        trainlist = [line for l in testlist[:i] + testlist[i + 1:] for line in l]
        assert type(trainlist) == list, 'this object has {} type.'.format(type(trainlist))

        # 学習
        features = train(trainlist, epoch)
        # assert type(features) == defaultdict, 'this object has {} type.'.format(type(features))
        pred_list = []  # ネガポジ判定結果格納用リスト
        for sentence in testlist[i]:  # testlist[i]: 検証用データ
            assert type(sentence) == str, 'this object has {} type.'.format(type(sentence))
            pred_list.append(check_pred(prediction_enhanced(sentence, features)))  # 予測
        print('正解率, 適合率, 再現率, F1スコア')
        score_list.append(calc_scores(Counter(pred_list), N))
        print(*calc_scores(Counter(pred_list), N), sep='\t')
        print('----------------------------------------')

    accuracy_average = (
                       score_list[0][0] + score_list[1][0] + score_list[2][0] + score_list[3][0] + score_list[4][0]) / C
    precision_average = (score_list[0][1] + score_list[1][1] + score_list[2][1] + score_list[3][1] + score_list[4][
        1]) / C
    recall_average = (score_list[0][2] + score_list[1][2] + score_list[2][2] + score_list[3][2] + score_list[4][2]) / C
    fscore_average = (score_list[0][3] + score_list[1][3] + score_list[2][3] + score_list[3][3] + score_list[4][3]) / C
    print('平均の正解率, 適合率, 再現率, F1スコア')
    print('{} {} {} {}'.format(accuracy_average, precision_average, recall_average, fscore_average))
