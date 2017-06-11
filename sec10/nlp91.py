outputfile = 'nlp91_output.txt'
fout = open(outputfile, 'wt')

with open('questions-words.txt') as f:
    sec = f.read().split(':')
    for i in range(0, len(sec)):
        if sec[i].split('\n')[0].strip() == 'family':
            print(sec[i].split('\n')[0].strip())
            print(*sec[i].split('\n')[1:], sep='\n', file=fout)

fout.close()
