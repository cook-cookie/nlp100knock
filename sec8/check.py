import re

with open('features.txt', 'r') as f:
    alphabet_list = []
    for line in f.readlines():
        m = re.search('^[a-zA-Z0-9]{3}$', line)
        if m:
            alphabet_list.append(m.group())

for word in sorted(alphabet_list):
    print(word)
