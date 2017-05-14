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

# vec("Spain") - vec("Madrid") + vec("Athens")とのコサイン類似度算出
vec = matrix_x300[dict_index_t['Spain']] - matrix_x300[dict_index_t['Madrid']] + matrix_x300[dict_index_t['Athens']]
distances = [cos_sim(vec, matrix_x300[i]) for i in range(0, len(dict_index_t))]

# 上位10件を表示
index_sorted = np.argsort(distances)
keys = list(dict_index_t.keys())
for index in index_sorted[:-11:-1]:
    print('{}\t{}'.format(keys[index], distances[index]))
