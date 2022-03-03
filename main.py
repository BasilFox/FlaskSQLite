from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Добавляем капитана
def main():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Victor"
    user.name = "Shrek"
    user.age = 53
    user.position = "captain assistant"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = "Shrek.bio@mars.org"
    user.hashed_password = "biolog"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Leopold"
    user.name = "Kishinevsky"
    user.age = 129
    user.position = "main pilot"
    user.speciality = "pilot"
    user.address = "module_3"
    user.email = "leopold.mold@mars.org"
    user.hashed_password = "pilotash"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Vladimir"
    user.name = "Skafovsky"
    user.age = 498
    user.position = "build manager"
    user.speciality = "builder"
    user.address = "module_4"
    user.email = "shkaf1533@mars.org"
    user.hashed_password = "shelf"
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
