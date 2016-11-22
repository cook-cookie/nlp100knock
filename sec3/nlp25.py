import re
from nlp20 import extract_json

dict = {}
lines = re.split(r"\n[\|}]", extract_json('イギリス'))

for line in lines:
    field = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if field is not None:
        dict[field.group(1)] = field.group(2)

for key, value in sorted(dict.items(), key=lambda x: x[1]):
    print(key, value)
