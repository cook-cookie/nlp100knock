import leveldb

if __name__ == '__main__':
    db = leveldb.LevelDB('./lvdb')
    count = 0

    for key, value in db.RangeIter():
        if value.decode() == 'Japan':
            count += 1
    print(count)