from LibraryManagementSystem import User, app, db
from flask import request
from DataParsing import create_response, display_data, response


def create_user():
    data = request.get_json()
    try:
        username = User.query.filter_by(username=data['username']).first()
        email = User.query.filter_by(email=data['email']).first()

        if username is None and email is None:
            user = User(firstname=data['firstname'],
                        lastname=data['lastname'],
                        username=data['username'],
                        email=data['email'],
                        cell_number=data['cell_number'],
                        address=data['address'])
            db.session.add(user)
            db.session.commit()
            return create_response("User Created")
        else:
            return create_response("User Already Exists")
    except KeyError:
        return create_response("Wrong data received!")


def search_user():
    if request.args.get('all'):
        users = User.query.all()

    elif request.args.get('firstname'):
        users = User.query.filter_by(firstname=request.args.get('firstname')).all()

    elif request.args.get('lastname'):
        users = User.query.filter_by(lastname=request.args.get('lastname')).all()

    elif request.args.get('username'):
        users = User.query.filter_by(username=request.args.get('username')).all()

    elif request.args.get('email'):
        users = User.query.filter_by(email=request.args.get('email')).all()

    elif request.args.get('cell_number'):
        users = User.query.filter_by(cell_number=request.args.get('cell_number')).all()

    elif request.args.get('address'):
        users = User.query.filter_by(address=request.args.get('address')).all()

    else:
        return create_response("Invalid Query")

    return response(users=users)


def update_user_data():
    if request.args.get('username'):
        update = User.query.filter_by(username=request.args.get('username')).first()

        if update:
            if request.args.get('firstname'):
                update.firstname = request.args.get('firstname')

            elif request.args.get('lastname'):
                update.lastname = request.args.get('lastname')

            elif request.args.get('change username'):
                check = User.query.filter_by(username=request.args.get('change username')).first()
                if check is None:
                    update.username = request.args.get('change username')
                else:
                    return create_response("User already exists!")

            elif request.args.get('email'):
                update.email = request.args.get('email')

            elif request.args.get('cell_number'):
                update.cell_number = request.args.get('cell_number')

            elif request.args.get('address'):
                update.address = request.args.get('address')

            else:
                return create_response("Invalid Query")

            db.session.commit()
            return create_response(display_data(user=update))

        else:
            return create_response("User does not exist")
    elif request.args.get('username') is None:
        return create_response("Invalid Query: Atrribute does not exist!")


def delete_user():
    if request.args.get('username'):
        user = User.query.filter_by(username=request.args.get('username')).first()

    elif request.args.get('email'):
        user = User.query.filter_by(email=request.args.get('email')).first()

    else:
        return create_response("Invalid Query! Delete using username or email only")

    if user:
        db.session.delete(user)
        db.session.commit()
        return create_response('User is deleted')
    else:
        return create_response("User does not exist")


if __name__ == '__main__':
    @app.route('/user', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def home():
        if request.method == 'POST':
            return create_user()

        elif request.method == 'GET':
            return search_user()

        elif request.method == 'PUT':
            return update_user_data()

        elif request.method == 'DELETE':
            return delete_user()

    app.run(debug=True)



