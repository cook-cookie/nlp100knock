import re
from collections import defaultdict

from MorphClass import Chunk, Morph
import pandas as pd


def morphChunk(filename):
    with open(filename) as f:
        sentences = []
        sentence = []
        chunk = Chunk()
        dic = defaultdict(list)
        for line in f.readlines():
            if line[0] == '*':
                sentence.append(chunk)
                chunk = Chunk()
                chunk.dst = int(line.split()[2][:-1])
                dic[chunk.dst].append(int(line.split()[1]))
                chunk.srcs = dic[int(line.split()[1])]
            else:
                if line.rstrip() == 'EOS':
                    sentence.append(chunk)
                    sentences.append(sentence[1:])
                    sentence = []
                    chunk = Chunk()
                    dic = defaultdict(list)
                else:
                    info = re.split('[,\t]', line.rstrip())
                    morph = Morph(info[0], info[7], info[1], info[2])
                    chunk.morphs.append(morph)

    return sentences


if __name__ == '__main__':
    df = pd.DataFrame([[''.join([morph.surface for morph in chunk.morphs]), str(chunk.dst)] for chunk in
                       morphChunk('neko.txt.cabocha')[7]], columns=['文節', '係り先'])
    print(df)
