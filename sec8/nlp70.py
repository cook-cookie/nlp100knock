import random


def check(filename='sentiment.txt'):
    counter_pos = 0
    counter_neg = 0

    with open(filename, 'r') as fr:
        for line in fr.readlines():
            if line[0] == '+':
                counter_pos += 1
            else:
                counter_neg += 1

    print('pos:{} neg:{}'.format(counter_pos, counter_neg))


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

    check('sentiment.txt')
    print('success!')
