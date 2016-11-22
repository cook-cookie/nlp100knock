import sys

with open(sys.argv[1]) as f:
    with open('hightemp_nlp11.txt', 'w') as f_out:
        f_out.write(f.read().expandtabs(1))