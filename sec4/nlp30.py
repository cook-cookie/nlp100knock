def tab_dict(tab_str: str) -> dict:
    lines = tab_str.split()
    if 0 < len(lines) < 4:
        return {'surface': lines[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': lines[0], 'base': lines[1], 'pos': lines[2], 'pos1': lines[3]}


def morphemes_list(morphemes: list) -> list:
    sentences = []
    sentence = []
    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences


with open('neko.txt.mecab') as f:
    morphemes = [tab_dict(line) for line in f]

sentences = morphemes_list(morphemes)

print(morphemes[::100])
print(sentences[::100])