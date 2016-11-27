from nlp30_ import inList

if __name__ == "__main__":
    for elem in inList('neko.txt.mecab_m'):
        for morphem in elem:
            if morphem['pos'] == '動詞':
                print(morphem['base'])