import bz2

filename_r10 = 'enwiki-20150112-400-r10-105752.txt'
filename_output = 'nlp80.txt'

if __name__ == '__main__':
    with open(filename_r10) as f, open(filename_output, mode='wt') as output:
        for line in f:
            line = line.rstrip()
            tokens = []
            for chunk in line.split(' '):
                token = chunk.strip('.,!?;:()[]\'"').strip()
                if len(token) > 0:
                    tokens.append(token)

            print(*tokens, sep=' ', end='\n', file=output)
