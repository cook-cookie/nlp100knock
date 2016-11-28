from pprint import pprint
import re


def inList(filename):
    with open(filename) as f:
        sentence = []
        sentences = []
        for line in f.readlines():
            info = re.split('[,\t]', line.rstrip())
            if info[0] != 'EOS':
                morpheme = {
                    'surface': info[0],
                    'base': info[7],
                    'pos': info[1],
                    'pos1': info[2]
                }
                sentence.append(morpheme)
                if morpheme['pos1'] == '句点':
                    sentences.append(sentence)
                    sentence = []

    return sentences


if __name__ == '__main__':
    pprint(inList('neko.txt.mecab_m'))
