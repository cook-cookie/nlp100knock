from nlp30_ import inList

if __name__ == '__main__':
    rensetsu = []
    for elem in inList('neko.txt.mecab_m'):
        nouns = []
        for morpheme in elem:
            if morpheme['pos'] == '名詞':
                nouns.append(morpheme['surface'])
            else:
                if len(nouns) > 1:
                    rensetsu.append("".join(nouns))
                nouns = []

        if len(nouns) > 1:
            rensetsu.append("".join(nouns))

    print(rensetsu)