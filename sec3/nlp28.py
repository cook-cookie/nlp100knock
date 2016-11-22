import re
from nlp20 import extract_json

def remove_markup(str):
    str = re.sub(r"'", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1", str)
    str = re.sub(r"</?.*?(\s)?/?>", r"", str)
    str = re.sub(r"\[.*\]", r"", str)
    return str

dict = {}
lines = re.split(r"\n[\|}]", extract_json('イギリス'))

for line in lines:
    field = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if field is not None:
        dict[field.group(1)] = remove_markup(field.group(2))

for key, value in sorted(dict.items(), key=lambda x: x[1]):
    print(key, value)
