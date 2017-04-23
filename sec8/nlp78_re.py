import codecs
import re
from nltk import stem
from nlp71 import make_stop_list
from collections import Counter


def check(str: str) -> bool:
    return str.lower() in stop_words


def extract_features(list_of_sentence: list) -> set:
    for sentence in list_of_sentence:
        for word in sentence[1:]:
            if check(word):  # ストップワード除去
                continue
            if re.search(r"[\[\]'/0-9]", word):  # 数字と記号を含むものを除去
                continue
            if re.search(r"(.)\1{2}", word):  # "xxx"のような同じアルファベットの連続を除去
                continue
            word = stemmer.stem(word)  # stemming
            if len(word) <= 2:  # 2文字以下は除去
                continue
            word_counter.update([word])

    features = [word for word, count in word_counter.items() if count >= 7]  # 出現回数6回以下は除去
    return set(features)


def labeling(list_of_sentence: list, set_of_features: set) -> list:
    list_of_features = []  # 文全体の1文ごとについての素性リスト
    for sentence in list_of_sentence:
        words = []
        for word in sentence[1:]:
            if check(word):  # ストップワード除去
                continue
            if re.search(r"[\[\]'/0-9]", word):  # 数字と記号を含むものを除去
                continue
            if re.search(r"(.)\1{2}", word):  # "xxx"のような同じアルファベットの連続を除去
                continue
            word = stemmer.stem(word)  # stemming
            if len(word) <= 2:  # 2文字以下は除去
                continue
            if word in set_of_features:
                words.append(word)
        if sentence[0] == '+1':
            features = '1 ' + ' '.join(words)
        else:
            features = '0 ' + ' '.join(words)
        list_of_features.append(features)

    return list_of_features


if __name__ == '__main__':
    stemmer = stem.PorterStemmer()
    word_counter = Counter()
    stop_words = make_stop_list()
    line_list = []

    with codecs.open('sentiment.txt') as f:
        for line in f:
            line_list.append(line.split())

    set_of_features = extract_features(line_list)
    with open('features_.txt', 'w') as fw:
        for elem in labeling(line_list, set_of_features):
            fw.write(elem + '\n')
            print(elem)
