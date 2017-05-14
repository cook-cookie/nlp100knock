from scipy import io
import sklearn.decomposition

fname_matrix_x = 'matrix_x'
fname_matrix_x300 = 'matrix_x300'

# 行列読み込み
matrix_x = io.loadmat(fname_matrix_x)['matrix_x']

# 次元圧縮
clf = sklearn.decomposition.TruncatedSVD(300)  # 疎行列に対応した主成分分析ツール
matrix_x300 = clf.fit_transform(matrix_x)  # 元の行列を入力して変換
io.savemat(fname_matrix_x300, {'matrix_x300': matrix_x300})
