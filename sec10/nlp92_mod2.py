from gensim.models import word2vec
import sys

sys.path.append('/mnt/diskA/romachi/PycharmProjects/nlp100knock')
from sec9_r10 import nlp89
from multiprocessing import Pool, Process
import multiprocessing as mp
import numpy as np
import pickle
import logging


def function(line_list: list) -> str:
    elem = line_list[1].split()
    vec_svd = nlp89.similar(matrix, dictionary, positive=[elem[1], elem[2]], negative=[elem[0]], topn=1)
    vec = model.most_similar(positive=[elem[1], elem[2]], negative=[elem[0]], topn=1)
    mod_sentence = line_list[1] + ' ' + vec_svd[0][0] + ' ' + '{:0.3f}'.format(vec_svd[0][1]) + ' ' + vec[0][
        0] + ' ' + '{:0.3f}'.format(vec[0][1]) + '\n'
    logging.info('{} line finished.'.format(line_list[0]))

    return mod_sentence


def multi(target_list: list) -> list:
    p = Pool(mp.cpu_count())
    result = p.map(function, enumerate(target_list, 1))
    p.close()
    return result


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = word2vec.Word2Vec.load('nlp90_train.model')

    with open('nlp91_output.txt', 'rt') as input_file:
        lines = [line.rstrip() for line in input_file]
    logging.info('Input file was all listed.')

    matrix = np.load('matrix_x300.npy')
    with open('dict_index_t', 'rb') as dict_file:
        dictionary = pickle.load(dict_file)
    logging.info('Matrix and Dictionary was loaded.')

    logging.info('Start list upping.')
    output_list = multi(lines)
    logging.info('List up was finished.')

    logging.info('Start writing.')
    with open('nlp92_output.txt', 'wt') as output_file:
        output_file.write(''.join(output_list))
    logging.info('Writing was finished.')
