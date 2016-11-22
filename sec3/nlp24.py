import re
from nlp20 import extract_json

if __name__ == '__main__':
    lines = extract_json('イギリス').split('\n')

    for line in lines:
        category = re.search("^\[\[(File|ファイル):(.*?)\|", line)
        if category is not None:
            print(category.group(2))
