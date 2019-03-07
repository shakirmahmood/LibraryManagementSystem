from LibraryManagementSystem import Book, app, db
from flask import request
from DataParsing import create_response, display_data, response


def create_book():
    data = request.get_json()
    try:
        isbn = Book.query.filter_by(isbn=data['isbn']).first()
        if isbn is None:
            book = Book(title=data['title'],
                        year=data['year'],
                        pages=data['pages'],
                        author=data['author'],
                        publisher=data['publisher'],
                        isbn=data['isbn'])

            db.session.add(book)
            db.session.commit()
            return create_response("Book Created")
        else:
            return create_response("Book already exists with the same ISBN. Pirated books are not allowed!")
    except KeyError:
        return create_response("Wrong data received!")


def search_book():
    if request.args.get('all'):
        books = Book.query.all()

    elif request.args.get('title'):
        books = Book.query.filter_by(title=request.args.get('title')).all()

    elif request.args.get('year'):
        books = Book.query.filter_by(year=request.args.get('year')).all()

    elif request.args.get('pages'):
        books = Book.query.filter_by(pages=request.args.get('pages')).all()

    elif request.args.get('author'):
        books = Book.query.filter_by(author=request.args.get('author')).all()

    elif request.args.get('publisher'):
        books = Book.query.filter_by(publisher=request.args.get('publisher')).all()

    elif request.args.get('isbn'):
        books = Book.query.filter_by(isbn=request.args.get('isbn')).all()

    else:
        return create_response("Invalid Query")

    return response(books=books)


def update_book_data():
    if request.args.get('isbn'):
        update = Book.query.filter_by(isbn=request.args.get('isbn')).first()

        if update:
            if request.args.get('title'):
                update.title = request.args.get('title')

            elif request.args.get('year'):
                update.year = request.args.get('year')

            elif request.args.get('pages'):
                update.pages = request.args.get('pages')

            elif request.args.get('author'):
                update.author = request.args.get('author')

            elif request.args.get('publisher'):
                update.publisher = request.args.get('publisher')

            # elif request.args.get('change isbn'):
            #     check = Book.query.filter_by(isbn=request.args.get('change isbn')).first()
            #     if check is None:
            #         update.isbn = request.args.get('change isbn')
            #     else:
            #         return create_response("Book already exists with the same ISBN. Pirated books are not allowed!")

            else:
                return create_response("Invalid Query")

            db.session.commit()
            return create_response(display_data(book=update))

        else:
            return create_response('Book is not available')
    elif request.args.get('isbn') is None:
        return create_response("Invalid Query: Atrribute does not exist!")


def delete_book():
    if request.args.get('isbn'):
        book = Book.query.filter_by(isbn=request.args.get('isbn')).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return create_response('Book is deleted')
        else:
            return create_response("Book does not exist already")

    else:
        return create_response("Invalid Query! Delete using ISBN only")


if __name__ == '__main__':
    @app.route('/book', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def home():
        if request.method == 'POST':
            return create_book()

        elif request.method == 'GET':
            return search_book()

        elif request.method == 'PUT':
            return update_book_data()

        elif request.method == 'DELETE':
            return delete_book()

    app.run(debug=True)



