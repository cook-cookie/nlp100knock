import sys

with open(sys.argv[1]) as f:
    print(len(f.readlines()))