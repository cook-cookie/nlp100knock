def cipher(target):
    result = ' '
    for str in target:
        if str.islower():
            result += chr(219 - ord(str))
        else:
            result += str

    return result

target = 'Little princess has no identity.'
print('原文:' + target)
print('暗号化:' + cipher(target))
print('復号化:' + cipher(cipher(target)))

target2 = input('文字列を入力:')
print('原文:' + target2)
print('暗号化:' + cipher(target2))
print('復号化:' + cipher(cipher(target2)))