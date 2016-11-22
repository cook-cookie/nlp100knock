set_col1 = set()
with open('col1.txt') as f:
    for line in f.readlines():
        set_col1.add(line)

for prefecture in sorted(set_col1):
    print(prefecture.rstrip())
