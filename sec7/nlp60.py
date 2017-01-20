import gzip
import json
import leveldb

if __name__ == '__main__':
    db = leveldb.LevelDB('./lvdb')

    with gzip.open(filename='artist.json.gz') as f:
        for line in f:
            data_json = json.loads(line.decode().rstrip())
            key = data_json['name'] + '\t' + str(data_json['id'])
            value = data_json.get('area')
            if value:
                db.Put(key.encode(), value.encode())