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

    plt.hist(
        counts,
        bins=20,
        range=(1, 20))

    plt.xlim(xmin=1, xmax=20)

    plt.title("ヒストグラム", fontproperties=fp)
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語の種類数', fontproperties=fp)

    plt.grid(axis='y')

    plt.show()
