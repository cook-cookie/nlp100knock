import sys
from collections import defaultdict

pref = defaultdict(int)

with open(sys.argv[1]) as f:
    line = f.readline()
    while line:
        pref[line.split()[0]] += 1
        line = f.readline()

for key, value in sorted(pref.items(), key = lambda x:x[1], reverse=True):
    print(key)