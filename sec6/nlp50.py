import re


def separate_by_sentence(filename='nlp.txt'):
    pattern = re.compile(r"(^.*?[\.|\;|\:|\!|\?])\s([A-Z].*)")
    with open(filename) as f:
        for line in f:
            line = line.strip()
            while len(line) > 0:
                match = pattern.match(line)
                if match:
                    yield match.group(1)
                    line = match.group(2)
                else:
                    yield line
                    line = ''


if __name__ == '__main__':
    for lines in separate_by_sentence():
        print(lines)
