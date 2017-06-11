import pickle
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'


def cos_sim(mat, dic, word_a: str, word_b: str):
    vec_a = mat[dic[word_a]]
    vec_b = mat[dic[word_b]]
    norm_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)

    if norm_ab != 0:
        return np.dot(vec_a, vec_b) / norm_ab
    else:
        # ベクトルのノルムが0だと似ているかどうかの判断すらできないので最低値
        return -1


if __name__ == '__main__':
    # 辞書読み込み
    with open(fname_dict_index_t, 'rb') as data_file:
        dict_index_t = pickle.load(data_file)

    # 行列読み込み
    matrix_x300 = np.load('matrix_x300.npy')

    print('{:0.3f}'.format(cos_sim(matrix_x300, dict_index_t, 'United_States', 'U.S')))
