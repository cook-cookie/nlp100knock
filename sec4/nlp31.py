import nlp30

surface = [morpheme['surface'] for morpheme in nlp30.morphemes if morpheme['pos1'].find('動詞') == 0]

print(surface[::100])
