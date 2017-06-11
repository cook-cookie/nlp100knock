import pickle
from collections import OrderedDict
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300.npy'
fname_countries = 'useList.txt'

fname_dict_new = 'dict_index_country'
fname_matrix_new = 'matrix_x300_country'

with open(fname_dict_index_t, 'rb') as data_file:
    dict_index_t = pickle.load(data_file)

matrix_x300 = np.load(fname_matrix_x300)

# 辞書にある用語のみの行列を作成
dict_new = OrderedDict()
matrix_new = np.empty([0, 300], dtype=np.float64)
count = 0

with open(fname_countries, 'rt') as f:
    for line in f:
        try:
            word = line.strip().replace(' ', '_')
            index = dict_index_t[word]
            matrix_new = np.vstack([matrix_new, matrix_x300[index]])
            dict_new[word] = count
            count += 1
        except:
            pass

# 結果の書き出し
np.save(fname_matrix_new, matrix_new)
with open(fname_dict_new, 'wb') as data_file:
    pickle.dump(dict_new, data_file)
