def n_gram(target, n):
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

set_x = set(n_gram('paraparaparadise', 2))
print('集合X:' + str(set_x))

set_y = set(n_gram('paragraph', 2))
print('集合Y:' + str(set_y))

print('和集合:' + str(set_x.union(set_y)))
print('差集合:' + str(set_x.difference(set_y)))
print('積集合:' + str(set_x.intersection(set_y)))
print('seは集合Xに含まれる:' + str('se' in set_x))
print('seは集合Yに含まれる:' + str('se' in set_y))
