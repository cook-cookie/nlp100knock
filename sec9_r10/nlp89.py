import pickle
from scipy import io
import numpy as np
from nlp87 import cos_sim

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'


def loaddict(filename: str) -> tuple:
    # 辞書読み込み
    with open(filename, 'rb') as data_file:
        dict_index_t = pickle.load(data_file)

    # 行列読み込み
    matrix_x300 = np.load('matrix_x300.npy')

    return (dict_index_t, matrix_x300)


def similar(mat, dict_index_t, positive: list, negative: list, topn: int = 10) -> list:
    # vec("Spain") - vec("Madrid") + vec("Athens")とのコサイン類似度算出
    vec = mat[dict_index_t[positive[0]]] - mat[dict_index_t[negative[0]]] + mat[dict_index_t[positive[1]]]
    distances = [cos_sim(vec, mat[i]) for i in range(0, len(dict_index_t))]
    # 上位topn件を表示
    index_sorted = np.argsort(distances)
    keys = list(dict_index_t.keys())
    returnlist = []
    for index in index_sorted[:-(topn + 1):-1]:
        returnlist.append((keys[index], distances[index]))

    return returnlist


if __name__ == '__main__':
    dict_index_t = loaddict(fname_dict_index_t)[0]
    matrix_x300 = loaddict(fname_dict_index_t)[1]

    vec = similar(matrix_x300, dict_index_t, positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
    for x in vec:
        print('{}\t{:0.3f}'.format(x[0], x[1]))
