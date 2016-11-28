from collections import Counter
from nlp30_ import inList
from matplotlib.font_manager import FontProperties
import pylab as plt

if __name__ == "__main__":
    counter = Counter()
    for elem in inList('neko.txt.mecab_m'):
        counter.update([morphem['surface'] for morphem in elem])

    size = 10
    list_word = counter.most_common(size)
    print(list_word)

    # 単語（x軸用）と出現数（y軸用）のリストに分解
    list_zipped = list(zip(*list_word))
    words = list_zipped[0]
    counts = list_zipped[1]

    fp = FontProperties(
        fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14
    )

    # 棒グラフのデータ指定
    plt.bar(
        range(0, size),  # x軸の値（0,1,2...9）
        counts,  # それに対応するy軸の値
        align='center'  # x軸における棒グラフの表示位置
    )

    # x軸のラベルの指定
    plt.xticks(
        range(0, size),  # x軸の値（0,1,2...9）
        words,  # それに対応するラベル
        fontproperties=fp  # 使うフォント情報
    )

    # x軸の値の範囲の調整
    plt.xlim(
        xmin=-1, xmax=size  # -1〜10（左右に1の余裕）
    )

    plt.title(
        '頻度上位10語',
        fontproperties=fp
    )
    plt.xlabel(
        '出現頻度が高い10語',
        fontproperties=fp
    )
    plt.ylabel(
        '出現頻度',
        fontproperties=fp
    )

    plt.grid(axis='y')

    plt.show()
