import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.mahasiswa


@app.route('/')
def ridho():

    _items = db.mahasiswa.find()
    items = [item for item in _items]

    return render_template('index.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'nama': request.form['nama'],
        'nim': request.form['nim'],
        'jurusan': request.form['jurusan'],
        'angkatan': request.form['angkatan'],
        'alamat': request.form['alamat'],
        'notelp': request.form['notelp']
    }
    db.mahasiswa.insert_one(item_doc)

    return redirect(url_for('ridho'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)