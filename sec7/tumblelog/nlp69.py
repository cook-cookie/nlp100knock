from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client.mgdb
collection = db.artist


@app.route('/')
def index():
    title = "artist"
    return render_template('index.html', title=title)


@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "artist"
    if request.method == 'POST':
        tag = request.form['tag']
        artist = [i for i in collection.find({"tags.value": tag})]
        artist = sorted(artist, key=lambda x: x["name"])
        return render_template('index.html', items=artist, title=title)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
