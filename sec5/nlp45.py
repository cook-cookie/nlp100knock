# predicate 述語
# research 調査する
# case 格

from nlp41 import morphChunk


def research_case():
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
                    if len(sentence[src].morphs) != 0 and '助詞' in sentence[src].morphs[-1].pos:
                        case.append(sentence[src].morphs[-1].surface)
                if len(case) != 0:
                    chunk_out = [pred, case]
                    sentence_out.append(chunk_out)
        sentences.append(sentence_out)

    return sentences


if __name__ == '__main__':
    for sentence in research_case():
        for chunk in sentence:
            print(chunk[0] + '\t' + ' '.join(sorted(chunk[1])))