from gensim.models import word2vec

fname_input = '../sec9/nlp81.txt'
data = word2vec.Text8Corpus(fname_input)
model = word2vec.Word2Vec(data, size=300)

out = model.most_similar(positive=[u'America'])
for x in out:
    print(x[0], x[1])
