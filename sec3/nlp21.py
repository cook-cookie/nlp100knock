import re
from nlp20 import extract_json

if __name__ == '__main__':
    lines = extract_json('イギリス').split('\n')

    # pattern = r"Category"
    # repatter = re.compile(pattern)

    for line in lines:
        if "Category" in line:
            print(line)
