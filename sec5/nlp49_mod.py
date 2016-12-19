import re
from itertools import combinations
from nlp41 import morphChunk


def replace_X(chunk):
    if '名詞' in [[morph.pos for morph in chunk.morphs]]:
        noun.append([index, re.sub('.*X', 'X', ''.join([morph.surface for morph in next_chunk.morphs]))])


def replace_Y(chunk):
    if '名詞' in [[morph.pos for morph in chunk.morphs]]:
        noun.append([index, re.sub('.*Y', 'Y', ''.join([morph.surface for morph in next_chunk.morphs]))])


def search_root(sentence):
    root_list = []
    for chunk_index, chunk in zip(range(len(sentence)), sentence):
        root_elem = [chunk_index]
        if not chunk.srcs:  # srcsが空のもののみリストに追加していく
            next_chunk = chunk
            while next_chunk.dst != -1:
                root_elem.append(next_chunk.dst)
                next_chunk = sentence[next_chunk.dst]
            root_list.append(root_elem)
    # (int in list) in list
    return root_list


def search_noun_pair(sentence):
    for chunk in sentence:
        if '名詞' == [morph.pos for morph in chunk.morphs]:
            noun_pair = [[morph.surface for morph in chunk.morphs]]

    #noun = []
    #for index, chunk in zip(range(len(sentence)), sentence):
    #    if '名詞' in [[morph.pos for morph in chunk.morphs]]:
    #        noun.append([index, re.sub('.*X', 'X', ''.join([morph.surface for morph in next_chunk.morphs]))])

if __name__ == '__main__':
    for sentence in morphChunk():
        for chunk in sentence:
            for morph in chunk.morphs[:]:
                if '記号' == morph.pos:
                    chunk.morphs.remove(morph)
        noun = []
        search_root(sentence)

        for cursor in combinations(noun, 2):
            for elem in cursor:
                for root_index, r in zip(range(len(noun)), root_list):
                    root_index_list = []
                    if elem[0] in r:
                        root_index_list.append(root_index)
                        if root_index_list[0] == root_index_list[1]:
                            print(' -> '.join([]))
                    else:
                        print('')
