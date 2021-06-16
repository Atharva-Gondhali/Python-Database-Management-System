from pickle import load
from pickle import dump


def if_user_exists(user):
    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()
    if user in acc:
        return True
    else:
        return False


def add_user(user, passwd):
    file = open("logger.pkl", "rb")
    acc = load(file)
    acc.update({user: passwd})
    file = open('logger.pkl', 'wb')
    dump(acc, file)
    file.close()


def check_passwd(user, passwd):
    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()
    if acc[user] == passwd:
        return True
    else:
        return False