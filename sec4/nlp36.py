from _operator import itemgetter
from collections import Counter
from pprint import pprint

from nlp30_ import inList


if __name__ == "__main__":
    total = 0
    counter = Counter()
    for elem in inList('neko.txt.mecab_m'):
        counter.update([morphem['base'] for morphem in elem])
        total += len(elem)

    for k, v in sorted(counter.most_common(), key=itemgetter(1, 0), reverse=True):
        print(k, v/total)
