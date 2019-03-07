from LibraryManagementSystem import app, db
from flask import request
from USER import create_user, delete_user, update_user_data, search_user
from BOOKS import create_book, search_book, update_book_data, delete_book
from ACQUIRE import acquire_book, return_book

db.init_app(app)
db.create_all()


@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user_data():
    if request.method == 'POST':
        return create_user()

    elif request.method == 'GET':
        return search_user()

    elif request.method == 'PUT':
        return update_user_data()

    elif request.method == 'DELETE':
        return delete_user()


@app.route('/book', methods=['GET', 'POST', 'DELETE', 'PUT'])
def book_data():
    if request.method == 'POST':
        return create_book()

    elif request.method == 'GET':
        return search_book()

    elif request.method == 'PUT':
        return update_book_data()

    elif request.method == 'DELETE':
        return delete_book()


@app.route('/acquire/<username>/<isbn>', methods=['POST', 'DELETE'])
def acquire_data(username, isbn):
    if request.method == 'POST':
        return acquire_book(username, isbn)

    elif request.method == 'DELETE':
        return return_book(isbn)


if __name__ == '__main__':
    app.run(debug=True)



