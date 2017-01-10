import re

def separate_by_sentence(filename='nlp.txt'):
    pattern = re.compile(r"(^.*?[\.|\;|\:|\!|\?])\s([A-Z].*)")
    with open(filename) as f:
        for line in f:


if __name__ == '__main__':
    separate_by_sentence()
