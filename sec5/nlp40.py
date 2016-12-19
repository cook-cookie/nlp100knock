from MorphClass import Morph
import re


def morphList(filename='neko.txt.cabocha'):
    with open(filename) as f:
        sentence = []
        sentences = []
        for line in f.readlines():
            if line[0] != '*':
                info = re.split('[,\t]', line.rstrip())
                if info[0] == 'EOS':
                    sentences.append(sentence)
                    sentence = []
                else:
                    morpheme = Morph(info[0], info[7], info[1], info[2])
                    sentence.append(morpheme)

    return sentences

if __name__ == '__main__':
    for sentence in morphList('neko.txt.cabocha')[2]:
        print(sentence.surface, sentence.base, sentence.pos, sentence.pos1)
