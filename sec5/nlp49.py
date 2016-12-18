import re
from itertools import combinations
from nlp41 import morphChunk


def search_noun():
    for sentence in morphChunk():
        for chunk in sentence:
            for morph in chunk.morphs[:]:
                if '記号' == morph.pos:
                    chunk.morphs.remove(morph)
        root_list = []
        noun = []
        for index, chunk in zip(range(len(sentence)), sentence):
            root_elem = [index]
            next_chunk = chunk
            if not chunk.srcs:  # srcsが空のもののみリストに追加していく
                while next_chunk.dst != -1:
                    root_elem.append(next_chunk.dst)
                    next_chunk = sentence[next_chunk.dst]
                root_list.append(root_elem)
            if '名詞' in [morph.pos for morph in chunk.morphs]:
                a = ''
                for morph in chunk.morphs:
                    if morph.pos == '名詞':
                        a += 'X'
                    else:
                        a += morph.surface
                noun.append([index, re.sub('.+X', 'X', a)])
        v1, v2 = [], []
        for cursor in combinations(noun, 2):
            belong_1, belong_2 = 0, 0
            flag = False
            for root_index, r in zip(range(len(root_list)), root_list):
                if cursor[0][0] in r and cursor[1][0] in r:
                    s = [cursor[0][1]]
                    next_cursor = cursor[0][0]
                    while sentence[next_cursor].dst != cursor[1][0]:
                        next_cursor = sentence[next_cursor].dst
                        s.append(''.join([morph.surface for morph in sentence[next_cursor].morphs]))
                    s.append('Y')
                    v2.append(' -> '.join(s))
                    flag = True
                    break
                if cursor[0][0] in r:
                    belong_1 = root_index
                if cursor[1][0] in r:
                    belong_2 = root_index
            if not flag:
                l1 = root_list[belong_1]
                l2 = root_list[belong_2]
                conect = [i for i in l1 if i in l2][0]
                s1 = [cursor[0][1]]
                next_cursor = cursor[0][0]
                while sentence[next_cursor].dst != conect:
                    next_cursor = sentence[next_cursor].dst
                    s1.append(''.join([morph.surface for morph in sentence[next_cursor].morphs]))
                s2 = [cursor[1][1].replace('X', 'Y')]
                next_cursor = cursor[1][0]
                while sentence[next_cursor].dst != conect:
                    next_cursor = sentence[next_cursor].dst
                    s2.append(''.join([morph.surface for morph in sentence[next_cursor].morphs]))
                s3 = ''.join([morph.surface for morph in sentence[conect].morphs])
                v1.append('{0} | {1} | {2}'.format(' -> '.join(s1), ' -> '.join(s2), s3))
        for line in v1:
            print(line)
        for line in v2:
            print(line)


if __name__ == '__main__':
    search_noun()
