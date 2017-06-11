from gensim.models import word2vec
import sys

sys.path.append('/mnt/diskA/romachi/PycharmProjects/nlp100knock')
sys.path.append('/mnt/diskA/romachi/PycharmProjects/nlp100knock/sec9_r10')
from sec9_r10 import nlp87_mod
from multiprocessing import Pool
import multiprocessing as mp
import numpy as np
import pickle
import logging
import time

matrix = np.load('matrix_x300.npy')
with open('dict_index_t', 'rb') as dict_file:
    dictionary = pickle.load(dict_file)


def function(line_elem: tuple) -> str:
    elem = line_elem[1].split('\t')
    sim_svd = nlp87_mod.cos_sim(matrix, dictionary, elem[0], elem[1])
    sim = model.similarity(elem[0], elem[1])
    mod_sentence = line_elem[1] + '\t' + '{:0.3f}'.format(sim_svd) + '\t' + '{:0.3f}'.format(sim) + '\n'
    logging.info('{} line finished.'.format(line_elem[0]))

    return mod_sentence


def multi(target_list: list) -> list:
    p = Pool(mp.cpu_count())
    result = p.map(function, list(enumerate(target_list, start=1)))
    p.close()
    return result


if __name__ == '__main__':
    start = time.time()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = word2vec.Word2Vec.load('nlp90_train.model')

    with open('combined.tab', 'rt') as input_file:
        lines = [line.rstrip() for line in input_file]
    logging.info('Input file was all listed.')

    logging.info('Matrix and Dictionary was loaded.')

    logging.info('Start list upping.')
    output_list = multi(lines)
    logging.info('List up was finished.')

    logging.info('Start writing.')
    with open('nlp94_output.txt', 'wt') as output_file:
        output_file.write(''.join(output_list))
    logging.info('Writing was finished.')
    elapsed_time = time.time() - start
    logging.info('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
