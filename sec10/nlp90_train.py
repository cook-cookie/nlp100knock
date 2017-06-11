from gensim.models import word2vec
import logging
import random

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# d = random.randint(1, 5)  # 文脈幅d

fname_input = '../sec9/nlp81.txt'
data = word2vec.Text8Corpus(fname_input)
model = word2vec.Word2Vec(data, size=300)
model.save('nlp90_train.model')

# out = model.most_similar(positive=[u'United_States'])
# for x in out:
#     print(x[0], x[1])
