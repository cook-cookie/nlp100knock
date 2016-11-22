import random

def Typoglycemia(target):
    result = []

    for word in target.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            change_list = list(word[1:-1])
            random.shuffle(change_list)
            result.append(word[0] + ''.join(change_list) + word[-1])

    return ' '.join(result)

target = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(Typoglycemia(target))
