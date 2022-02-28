
from data.users import User
from data.job import Jobs
from data.db_session import global_init, create_session


def main():
    db_name = input()
    # db_name = "db/blogs.sqlite"
    global_init(db_name)
    db_sess = create_session()

    for user in db_sess.query(User).filter(User.address == 'module_1', User.age >= 21):
        print(user)
        user.address = 'module_3'
    db_sess.commit()


if __name__ == '__main__':
    main()