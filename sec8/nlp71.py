def check(str: str) -> bool:
    return str.lower() in stop_words


if __name__ == '__main__':
    stop_list = []  # Ranks.lnによるStop wordのリスト

    with open('stop_words.txt', 'r') as f:
        for word in f.readlines():
            stop_list.append(word.rstrip())

    stop_words = set(stop_list)
    print(stop_words)

    # 正しく検出されることのテスト
    assert check('a')  # リストの先頭
    assert check('your')  # リストの末尾
    assert check('on')  # リストの中間
    assert check('A')  # 大小文字の同一視
    assert check('Your')  # 大小文字の同一視
    assert check('ON')  # 大小文字の同一視

    # 誤検出されないことのテスト
    assert not check('0')  # リストにない
    assert not check('z')  # リストにない
    assert not check('bout')  # 後方一致されない
    assert not check('acros')  # 前方一致されない
    assert not check('fte')  # 中間一致されない
    assert not check(' ')  # 空白
    assert not check('\n')  # 制御コード
    assert not check('')  # 空文字
