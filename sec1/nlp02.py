str1 = 'パトカー'
str2 = 'タクシー'
str3 = ''

for x, y in zip(str1, str2):
    str3 = str3 + x + y

print(str3)