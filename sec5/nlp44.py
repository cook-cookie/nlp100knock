from graphviz import Digraph
from nlp41 import morphChunk


def genNode(sentenceNum=5):
    G = Digraph(format='png')
    G.attr('node', shape='circle')

    for chunk in morphChunk()[sentenceNum]:
        s = ''.join([morph.surface for morph in chunk.morphs])
        if chunk.dst != -1:
            l = ''.join([morph.surface for morph in morphChunk()[sentenceNum][chunk.dst].morphs])
            G.edge(s, l)

    print(G)
    G.render('nlp44_sentence' + str(sentenceNum))


if __name__ == '__main__':
    genNode(10)
