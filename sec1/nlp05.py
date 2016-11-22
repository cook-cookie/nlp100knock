def n_gram(target, n):
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

if __name__ == '__main__':
    target = 'I am an NLPer'
    words = target.split(' ')

    result = n_gram(target, 2)
    print(result)

    result = n_gram(words, 2)
    print(result)
