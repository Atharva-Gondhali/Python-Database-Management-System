import mysql.connector
from pickle import load, dump

file = open("back_info.pkl", "rb")
info = load(file)
file.close()

mydb = mysql.connector.connect(
    host=info[0],
    user=info[1],
    passwd=info[2])

my_cursor = mydb.cursor()


def delete_user(user):
    db_name = user.lower().replace(" ", "") + "db"
    my_cursor.execute(f"DROP DATABASE {db_name}")
    my_cursor.close()
    mydb.close()

    file = open("logger.pkl", "rb")
    acc = load(file)
    del acc[user]

    file = open("logger.pkl", "wb")
    dump(acc, file)
    file.close()


def change_password(user, password):
    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()

    acc[user] = password

    file = open("logger.pkl", "wb")
    dump(acc, file)
    file.close()
