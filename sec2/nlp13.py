import sys


def merge_col(src_lines1, src_lines2, output):
    col = []
    for col1, col2 in zip(src_lines1, src_lines2):
        col.append('\t'.join([col1.rstrip(), col2]))
    with open(output, 'w') as f_out:
        f_out.writelines(col)


with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

merge_col(lines1, lines2, 'col_merge.txt')