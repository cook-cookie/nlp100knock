import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client['mgdb']
    collection = db.artist

    dancers = []
    for col in collection.find({'tags.value': 'dance'}):
        if 'rating' in col:
            dancers.append([col['name'], col['rating']['count']])

    dancers_sorted = sorted(dancers, key=lambda x: x[1], reverse=True)
    for i, value in enumerate(dancers_sorted):
        if i < 10:
            print(value[0], value[1])