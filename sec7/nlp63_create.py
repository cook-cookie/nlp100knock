import gzip
import json
import leveldb
import pickle

if __name__ == '__main__':
    db = leveldb.LevelDB('./lvdb2')

    with gzip.open(filename='artist.json.gz') as f:
        for line in f:
            data_json = json.loads(line.decode().rstrip())
            key = data_json['name']
            value = pickle.dumps(data_json.get('tags'))
            if value:
                db.Put(key.encode(), value)
