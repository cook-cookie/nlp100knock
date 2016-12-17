from nlp41 import morphChunk

def extract_pass():
    for sentence in morphChunk():
        for chunk in sentence:
            for morph in chunk.morphs[:]:
                if '記号' == morph.pos:
                    chunk.morphs.remove(morph)
        for chunk in sentence:
            if '名詞' in {morph.pos for morph in chunk.morphs}:
                s = []
                next_chunk = chunk
                while next_chunk.dst != -1:
                    s.append(''.join([morph.surface for morph in next_chunk.morphs]))
                    next_chunk = sentence[next_chunk.dst]
                s.append(''.join([morph.surface for morph in next_chunk.morphs]))
                if len(s) != 1:
                    print(' -> '.join(s))


if __name__ == '__main__':
    extract_pass()