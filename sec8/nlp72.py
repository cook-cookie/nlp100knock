import re
from nltk import stem
from nlp71 import make_stop_list
from collections import Counter


def check(str: str) -> bool:
    return str.lower() in stop_words


if __name__ == '__main__':
    stemmer = stem.PorterStemmer()
    word_counter = Counter()
    stop_words = make_stop_list()

    with open('sentiment.txt', 'rb') as fs:
        for line in fs.readlines():
            for word in line.decode()[3:].split(' '):
                word = word.strip()
                if check(word):  # ストップワード除去
                    continue
                word = stemmer.stem(word)  # stemming
                if len(word) <= 2:  # 2文字以下は除去
                    continue
                if re.search(r"[\[\]'/0-9]", word):
                    continue
                word_counter.update([word])

        candidate = [word for word, count in word_counter.items() if count >= 6]

    with open('identities.txt', 'w') as fw:
        print(*candidate, sep='\n', file=fw)