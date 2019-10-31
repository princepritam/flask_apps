from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os, code
app = Flask(__name__)
app.config['APP_SETTINGS'] = os.environ['APP_SETTINGS']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/test_db'
db = SQLAlchemy(app)

from models import *

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_book():
    name=request.get_json()['name']
    author=request.get_json()['author']
    published=request.get_json()['published']
    try:
        book=Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return "Book is added. book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        books=Book.query.all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book=Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run(debug=True, host='localhost')