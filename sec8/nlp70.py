import random

if __name__ == '__main__':
    write_list = []
    with open('rt-polaritydata/rt-polarity.pos', 'rb') as f:
        for line in f.readlines():
            write_list.append('{} {}'.format('+1', line.decode(encoding='iso-8859-1')))

    with open('rt-polaritydata/rt-polarity.neg', 'rb') as f:
        for line in f.readlines():
            write_list.append('{} {}'.format('-1', line.decode(encoding='iso-8859-1')))

    # list = random.shuffle(write_list)
    # for line in list:
    #     print(line)

    random.shuffle(write_list)
    with open('sentiment.txt', 'w') as fs:
        for line in write_list:
            fs.write(line)
