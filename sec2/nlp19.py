import sys
from collections import Counter

with open(sys.argv[1]) as f:
    lines = f.readlines()

col = []
for line in lines:
    col.append(line.split()[0])
counter = Counter(col)

for line in sorted(counter, key=lambda pref: Counter(pref.split()[0]).most_common(), reverse=False):
    print(counter, line.rstrip())