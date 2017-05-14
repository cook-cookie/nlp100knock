import pickle
from scipy import io
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'


def cos_sim(vec_a, vec_b):
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
    matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

    # 'United States'と'U.S'のコサイン類似度表示
    vec_a = matrix_x300[dict_index_t['United_States']]
    vec_b = matrix_x300[dict_index_t['U.S']]

    print(cos_sim(vec_a, vec_b))
