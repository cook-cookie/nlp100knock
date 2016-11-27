from collections import Counter
from nlp30_ import inList

if __name__ == "__main__":
    counter = Counter()
    for elem in inList('neko.txt.mecab_m'):
        counter.update([morphem['surface'] for morphem in elem])

    print(counter.most_common())
