import pickle
from scipy import io
import numpy as np
from nlp87 import cos_sim

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'

# 辞書読み込み
with open(fname_dict_index_t, 'rb') as data_file:
    dict_index_t = pickle.load(data_file)

# 行列読み込み
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

# 'England'とのコサイン類似度算出
vec_England = matrix_x300[dict_index_t['England']]
distances = [cos_sim(vec_England, matrix_x300[i]) for i in range(0, len(dict_index_t))]

# 上位10件を表示
index_sorted = np.argsort(distances)
keys = list(dict_index_t.keys())
for index in index_sorted[-2:-12:-1]:  # トップに来る自分自身は除く
    print('{}\t{}'.format(keys[index], distances[index]))
