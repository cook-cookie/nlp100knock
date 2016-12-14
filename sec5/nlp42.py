import re

from nlp41 import morphChunk

if __name__ == '__main__':
    sentences = morphChunk()
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                print(''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']) + '\t' +
                      ''.join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号']))
