from gensim.models import word2vec
import logging
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load('nlp90_train.model')
argvs = sys.argv
print(model.similarity(argvs[1], argvs[2]))
