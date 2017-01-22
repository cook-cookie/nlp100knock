import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client['mgdb']
    collection = db.artist
    count = 0

    for col in collection.find({'name': 'Queen'}):
        print(col)