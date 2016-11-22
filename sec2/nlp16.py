import sys


def n_split(target, split_number):
    if split_number != 0:
        with open(target) as f:
            lines = f.readlines()

        if (len(lines) % split_number == 0):
            part_num = len(lines) / split_number
            for i in range(split_number):
                with open('split_%s.txt' % str(i + 1), 'w') as f_out:
                    f_out.writelines(lines[part_num * i: part_num * (i + 1)])
        else:
            print('Sorry, please enter the number that does not remain.')
    else:
        print('===ZeroDivisionError===')


n_split(sys.argv[1], int(sys.argv[2]))
