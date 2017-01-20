import leveldb

if __name__ == '__main__':
    db = leveldb.LevelDB('./lvdb')

    while True:
        try:
            s = input('enter artist name: ')
            print(db.Get(s.encode()).decode())
        except KeyError:
            print('error')
        except KeyboardInterrupt:
            exit(0)
