import pickle

if __name__ == '__main__':
    s = pickle.load(open('nlp73_pickle', 'rb'))
    print('低いやつtop10')
    for word in [(k, v) for k, v in sorted(s.items(), key=lambda x: x[1])][:10]:
        print(word)
    print('高いやつtop10')
    for word in [(k, v) for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)][:10]:
        print(word)
