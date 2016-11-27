from collections import Counter
from nlp30_ import inList
from matplotlib.font_manager import FontProperties
import pylab as plt

if __name__ == "__main__":
    counter = Counter()
    for elem in inList('neko.txt.mecab_m'):
        counter.update([morphem['surface'] for morphem in elem])

    list_word = counter.most_common()

    # 出現数のリスト取得
    counts = list(zip(*list_word))[1]

    # グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
    fp = FontProperties(
        fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14
    )

    # 散布図のデータ指定
    plt.scatter(
        range(1, len(counts) + 1),  # x軸：順位
        counts  # y軸：出現頻度
    )

    # 軸の値の範囲の調整
    plt.xlim(1, len(counts) + 1)
    plt.ylim(1, counts[0])

    # 対数グラフに
    plt.xscale('log')
    plt.yscale('log')

    # グラフのタイトル、ラベル指定
    plt.title("39. Zipfの法則", fontproperties=fp)
    plt.xlabel('出現度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)

    # グリッドを表示
    plt.grid(axis='both')

    # 表示
    plt.show()