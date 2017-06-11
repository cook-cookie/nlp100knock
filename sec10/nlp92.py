from gensim.models import word2vec
import pickle
import numpy as np
from nlp87 import cos_sim
from sec9_r10 import nlp89
# import logging
import math

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load('nlp90_train.model')
fname_dict_index_t = '../sec9_r10/dict_index_t'
fname_matrix_x300 = '../sec9_r10/matrix_x300'

nlp89.loaddict(fname_dict_index_t)
dict_index_t = nlp89.loaddict(fname_dict_index_t)[0]
matrix_x300 = nlp89.loaddict(fname_dict_index_t)[1]

with open('nlp91_output.txt', 'rt') as f:
    # temp = [line.rstrip() for line in f]
    for line in f:
        # line2 - line1 + line3
        vec85 = nlp89.similar(matrix_x300, dict_index_t, positive=[line.split()[1], line.split()[2]],
                              negative=[line.split()[0]], topn=1)
        vec90 = model.most_similar(positive=[line.split()[1], line.split()[2]], negative=[line.split()[0]], topn=1)
        # print('{}\t{:0.3f}\t{}\t{:0.3f}'.format(vec85[0][0], vec85[0][1], vec90[0][0], vec90[0][1]))
        temp = line.split()
        temp.append(vec85[0][0])
        temp.append(str(vec85[0][1]))
        temp.append(vec90[0][0])
        temp.append(str(vec90[0][1]))
        with open('nlp91_output_mod.txt', 'wt') as f_out:
            f_out.write(' '.join(temp) + '\n')
