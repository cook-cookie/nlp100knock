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

    # ヒストグラムのデータ指定
    plt.hist(
        counts,  # データのリスト
        bins=20,  # ビンの数
        range=(1, 20))  # 値の範囲

    # x軸の値の範囲の調整
    plt.xlim(xmin=1, xmax=20)

    # グラフのタイトル、ラベル指定
    plt.title("38. ヒストグラム", fontproperties=fp)
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語の種類数', fontproperties=fp)

    # グリッドを表示
    plt.grid(axis='y')

    # 表示
    plt.show()
