from _operator import itemgetter
from collections import Counter
from pprint import pprint

from nlp30_ import inList
from matplotlib.font_manager import FontProperties
import pylab as plt

if __name__ == "__main__":
    counter = Counter()
    total = 0
    for elem in inList('neko.txt.mecab_m'):
        counter.update([morphem['base'] for morphem in elem])
        total += len(elem)

    counts = []
    for k, v in sorted(counter.most_common(), key=itemgetter(1, 0), reverse=True):
        counts.append(v/total)

    pprint(counts)
    #list_word = counter.most_common()

    #counts = list(zip(*list_word))[1] / total

    fp = FontProperties(
        fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14
    )

    plt.hist(
        counts,
        bins=20,
        histtype='step',
        linewidth=3
        )

    #plt.xlim(xmin=1, xmax=20)

    plt.title("ヒストグラム", fontproperties=fp)
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語の種類数', fontproperties=fp)

    plt.grid(axis='y')

    plt.show()
