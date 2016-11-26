import nlp30

sahen = [morpheme['surface'] for morpheme in nlp30.morphemes if morpheme['pos1'] == '名詞-サ変接続']

print(sahen[::100])
