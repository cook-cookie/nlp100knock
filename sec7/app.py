import pymongo
import re

import bottle
from bottle import route, run, template, request

bottle.debug(True)

client = pymongo.MongoClient('localhost', 27017)
db = client.mgdb
collection = db.artist


@route('/')
def html_index():
    return template('index')


@route('/', method='POST')
def search():
    artist_name = request.forms.artist_name
    genre = request.forms.genre

    global collection
    buf = ''

    for aliases in collection.find({'tags.value': re.compile(genre, re.IGNORECASE)}):
        buf += str(aliases)
    return buf

    # return template('{{name}}, {{genre}}', name=artist_name, genre=genre)


if __name__ == '__main__':
    run(host='localhost', port=9999)
