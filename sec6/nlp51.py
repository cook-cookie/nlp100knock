from nlp50 import separate_by_sentence


def separate_by_space(sentence):
    words = sentence.split()
    for word in words:
        yield word


if __name__ == '__main__':
    for sentence in separate_by_sentence():
        for word in separate_by_space(sentence):
            print(word)
        print('')
