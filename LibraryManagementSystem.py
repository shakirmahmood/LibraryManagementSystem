from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'LMS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    cell_number = db.Column(db.Integer)
    address = db.Column(db.String(64))
    # Acquire = db.relationship('Acquire', backref='UserAcquire', lazy='dynamic')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    author = db.Column(db.String(64))
    publisher = db.Column(db.String(64))
    isbn = db.Column(db.Integer, unique=True)
    # Acquire = db.relationship('Acquire', backref='BookAcquire', lazy='dynamic')


class Acquire(db.Model):
    __tablename__ = 'acquire'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64))
    booktitle = db.Column(db.String(64))
    bookyear = db.Column(db.Integer)
    bookpages = db.Column(db.Integer)
    bookauthor = db.Column(db.String(64))
    bookpublisher = db.Column(db.String(64))
    bookisbn = db.Column(db.Integer, unique=True)

# db.create_all()






