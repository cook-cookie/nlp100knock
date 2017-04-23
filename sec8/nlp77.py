from collections import Counter


def return_tpfpfntn(sentence: str) -> str:
    if sentence.split('\t')[1] == '+1':
        return 'TP' if sentence.split('\t')[0] == '+1' else 'FP'
    else:
        return 'FN' if sentence.split('\t')[0] == '+1' else 'TN'


def calc_scores(counts: dict, N: int) -> tuple:
    accuracy = (counts['TP'] + counts['TN']) / N
    precision = counts['TP'] / (counts['TP'] + counts['FP'])
    recall = counts['TP'] / (counts['TP'] + counts['FN'])
    fscore = 2 * recall * precision / (recall + precision)

    return accuracy, precision, recall, fscore

if __name__ == '__main__':
    with open('nlp76_output.txt') as f:
        fi = f.readlines()

    N = len(fi)

    pred_list = []

    for sentence in fi:
        pred_list.append(return_tpfpfntn(sentence))

    print('正解率, 適合率, 再現率, F1スコア')
    print(*calc_scores(Counter(pred_list), N), sep='\t')
