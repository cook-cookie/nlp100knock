import numpy as np

with open('nlp94_output.txt', 'rt') as f:
    lines = [line.rstrip() for line in f]
    human_score = []
    svd_score = []
    w2v_score = []
    len_lines = len(lines)

    for line in lines:
        elem = line.split('\t')
        human_score.append(float(elem[2]))
        svd_score.append(float(elem[3]))
        w2v_score.append(float(elem[4]))

# ソート
human_index_sorted = np.argsort(human_score)
svd_index_sorted = np.argsort(svd_score)
w2v_index_sorted = np.argsort(w2v_score)

# 順位の配列作成
human_order = [0] * len_lines
svd_order = [0] * len_lines
w2v_order = [0] * len_lines
for i in range(len_lines):
    human_order[human_index_sorted[i]] = i
    svd_order[svd_index_sorted[i]] = i
    w2v_order[w2v_index_sorted[i]] = i

# スピアマン相関係数計算
total_sh = 0
total_wh = 0
for i in range(len_lines):
    total_sh += pow(human_order[i] - svd_order[i], 2)
    total_wh += pow(human_order[i] - w2v_order[i], 2)
result_sh = 1 - (6 * total_sh) / (pow(len_lines, 3) - len_lines)
result_wh = 1 - (6 * total_wh) / (pow(len_lines, 3) - len_lines)

print('svd-human score :{:0.3f}'.format(result_sh))
print('w2v-human score :{:0.3f}'.format(result_wh))
