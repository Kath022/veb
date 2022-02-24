from flask import Flask
from data.users import User
from data.db_session import global_init, create_session

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_name = input()
    # db_name = "db/blogs.sqlite"
    global_init(db_name)
    db_sess = create_session()

    for user in db_sess.query(User).filter(User.address == 'module_1',
                                           User.speciality.notlike('engineer'),
                                           User.position.notlike('engineer')):
        print(user.id)


if __name__ == '__main__':
    main()