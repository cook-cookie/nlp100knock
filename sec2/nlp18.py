import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in sorted(lines, key=lambda temp: temp.split()[2], reverse=True):
    print(line.rstrip())
