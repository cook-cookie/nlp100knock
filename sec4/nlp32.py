import nlp30

base = [morpheme['base'] for morpheme in nlp30.morphemes if morpheme['pos1'].find('動詞') == 0]

print(base[::100])
