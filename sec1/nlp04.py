target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
num_first_only = (1, 5, 6, 7, 8, 9, 15, 16)
result = {}

words = target.split(' ')
for key, value in zip(words, range(1, len(words))):
    if value in num_first_only:
        result[key[0]] = value
    else:
        result[key[:2]] = value

print(result)
