from gensim.models import word2vec
# import logging
import math

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec.load('nlp90_train.model')
print('nlp86:')
print(model['United_States'])

print()
print('nlp87:')
print(model.similarity('United_States', 'U.S'))
print(type(model.similarity('United_States', 'U.S')))

print()
print('nlp88:')
out = model.most_similar(positive=['England'])
for x in out:
    print(x[0], '{:0.3f}'.format(x[1]))
print()
print('nlp89:')
vec = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=5)
for x in vec:
    print(x[0], '{:0.3f}'.format(x[1]))
    # print(x[0], round(x[1]))
