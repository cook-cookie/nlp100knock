# predicate 述語
# research 調査する
# case 格
from operator import itemgetter

from nlp41 import morphChunk


def research_case_mod():
    sentences = []
    for sentence in morphChunk():
        sentence_out = []
        for chunk in sentence:
            for morph in chunk.morphs[:]:
                if '記号' == morph.pos:
                    chunk.morphs.remove(morph)
        for chunk in sentence:
            if '動詞' in [morph.pos for morph in chunk.morphs]:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        pred = morph.base
                        break
                case = []
                for src in chunk.srcs:
                    # if '助詞' in [morph.pos for morph in sentence[src].morphs[-1]]:
                    case_frame = []
                    if len(sentence[src].morphs) != 0 and '助詞' in sentence[src].morphs[-1].pos:
                        case_frame.append(sentence[src].morphs[-1].surface)
                        case_frame.append(''.join([morph.surface for morph in sentence[src].morphs]))
                        case.append(case_frame)
                if len(case) != 0:
                    case.sort()
                    chunk_out = [pred, case]
                    sentence_out.append(chunk_out)
        sentences.append(sentence_out)

    return sentences


if __name__ == '__main__':
    for sentence in research_case_mod():
        for chunk in sentence:
            # print(chunk[0] + '\t' + ' '.join(sorted(chunk[1], key=lambda x:x[0])))
            print(chunk[0] +
                  '\t' + ' '.join([v[0] for v in chunk[1]]) +
                  '\t' + ' '.join([v[1] for v in chunk[1]]))
