import pickle
import leveldb

if __name__ == '__main__':
    db = leveldb.LevelDB('./lvdb2')

    while True:
        try:
            s = input('enter artist name: ')
            for elem in pickle.loads(db.Get(s.encode())):
                print('value: ' + elem['value'])
                print('count: ' + str(elem['count']))
        except KeyError:
            print('error')
        except KeyboardInterrupt:
            exit(0)
