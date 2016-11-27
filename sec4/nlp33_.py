from nlp30_ import inList

if __name__ == "__main__":
    for elem in inList('neko.txt.mecab_m'):
        for morphem in elem:
            if morphem['pos'] == '名詞' and morphem['pos1'] == 'サ変接続':
                print(morphem['surface'])