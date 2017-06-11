from collections import Counter

if __name__ == '__main__':
    count_svd = 0
    count_w2v = 0

    with open('nlp92_output2.txt') as f:
        lines = [line.rstrip() for line in f]
        len_lines = len(lines)
        for line in lines:
            elem = line.split()
            # print(type(elem[3]))
            # print(type(elem[6]))
            if elem[3] == elem[4]:
                count_svd += 1
            if elem[3] == elem[6]:
                count_w2v += 1

    print('{}/{}'.format(count_svd, len_lines))
    print('accuracy(svd): {:0.3f}'.format(count_svd / len_lines))
    print('{}/{}'.format(count_w2v, len_lines))
    print('accuracy(w2v): {:0.3f}'.format(count_w2v / len_lines))
