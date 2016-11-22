import sys


def col_out(src_lines, col_number, output):
    col = []
    for line in src_lines:
        col.append(line.split('\t')[col_number] + '\n')
    with open(output, 'w') as f_out:
        f_out.writelines(col)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    col_out(lines, 0, 'col1.txt')
    col_out(lines, 1, 'col2.txt')