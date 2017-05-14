import bz2

filename_r100 = 'enwiki-20150112-400-r100-10576.txt'
filename_output = 'nlp80.txt'

if __name__ == '__main__':
    with open(filename_r100) as f, open(filename_output, mode='wt') as output:
        for line in f:
            line = line.rstrip()
            tokens = []
            for chunk in line.split(' '):
                token = chunk.strip('.,!?;:()[]\'"').strip()
                if len(token) > 0:
                    tokens.append(token)

            print(*tokens, sep=' ', end='\n', file=output)
