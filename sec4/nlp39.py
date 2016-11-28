from collections import Counter
from nlp30_ import inList
from matplotlib.font_manager import FontProperties
import pylab as plt

if __name__ == "__main__":
    counter = Counter()
    for elem in inList('neko.txt.mecab_m'):
        counter.update([morphem['surface'] for morphem in elem])

    list_word = counter.most_common()

    counts = list(zip(*list_word))[1]

    fp = FontProperties(
        fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14
    )

    plt.scatter(
        range(1, len(counts) + 1),
        counts
    )

    plt.xlim(1, len(counts) + 1)
    plt.ylim(1, counts[0])

    plt.xscale('log')
    plt.yscale('log')

    plt.title("Zipfの法則", fontproperties=fp)
    plt.xlabel('出現度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)

    plt.grid(axis='both')

    plt.show()