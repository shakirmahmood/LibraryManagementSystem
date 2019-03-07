from LibraryManagementSystem import User, Book, Acquire, app, db
from DataParsing import create_response


def acquire_book(username, isbn):
    user = User.query.filter_by(username=username).first()
    book = Book.query.filter_by(isbn=isbn).first()

    if book is None or user is None:
        return create_response("Sorry! The book/user is not present")

    acquired = Acquire(booktitle=book.title,
                       bookyear=book.year,
                       bookpages=book.pages,
                       bookauthor=book.author,
                       bookpublisher=book.publisher,
                       bookisbn=book.isbn,
                       user=user.username)
    db.session.add(acquired)

    book = Book.query.filter_by(isbn=isbn).first()
    db.session.delete(book)

    db.session.commit()
    return create_response("Book Acquired")


def return_book(isbn):
    acquired = Acquire.query.filter_by(bookisbn=isbn).first()
    if acquired is None:
        return create_response("Book is not acquired")
    temp_book = Book(title=acquired.booktitle,
                     year=acquired.bookyear,
                     pages=acquired.bookpages,
                     author=acquired.bookauthor,
                     publisher=acquired.bookpublisher,
                     isbn=acquired.bookisbn)
    db.session.delete(acquired)
    db.session.add(temp_book)
    db.session.commit()

    return create_response("Book Returned")


if __name__ == '__main__':
    app.run(debug=True)



