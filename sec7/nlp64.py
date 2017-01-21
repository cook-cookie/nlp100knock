import gzip
import json
import pymongo
from pymongo import MongoClient

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client['mgdb']
    collection = db.artist
    count = 0

    print('データベース作成開始')
    with gzip.open(filename='artist.json.gz') as f:
        bulk_list = []
        for line in f:
            data_json = json.loads(line.decode().rstrip())
            bulk_list.append(data_json)
            count += 1
            if count % 10000 == 0:
                print('{}件登録中'.format(count))
        collection.insert_many(bulk_list)
        print('{}件登録完了'.format(count))

    print('インデックス作成開始')
    collection.create_index([('name', pymongo.ASCENDING)])
    collection.create_index([('aliases.name', pymongo.ASCENDING)])
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])
    print('インデックス作成完了')