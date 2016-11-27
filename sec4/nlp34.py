from nlp30_ import inList

if __name__ == "__main__":
    AnoB = []
    for elem in inList('neko.txt.mecab_m'):
        if len(elem) > 2:
            for i in range(1, len(elem) - 1):
                if elem[i]['surface'] == 'の' \
                        and elem[i - 1]['pos'] == '名詞' \
                        and elem[i + 1]['pos'] == '名詞':
                    AnoB.append(elem[i - 1]['surface'] + 'の' + elem[i + 1]['surface'])

    print(AnoB)
