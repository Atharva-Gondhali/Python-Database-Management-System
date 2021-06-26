import mysql.connector
from pickle import load
from pickle import dump


def login_db( user ):
    db_name = user.lower() + "db"

    # file = open("back_info.pkl", "rb")
    # info = load(file)
    # file.close
    # info[3] = db_name
    # file = open('logger.pkl', 'wb')
    # dump(info, file)
    # file.close()

    return db_name


def if_user_exists(user):
    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()
    if user in acc:
        return True
    else:
        return False


def add_user(user, passwd):
    file = open("back_info.pkl", "rb")
    info = load(file)
    file.close()

    mydb = mysql.connector.connect(
        host=info[0],
        user=info[1],
        passwd=info[2])

    my_cursor = mydb.cursor()

    db_name = user.replace(" ", "") + "db"
    my_cursor.execute(f"CREATE DATABASE {db_name}")

    my_cursor.close()
    mydb.close()

    mydb = mysql.connector.connect(
        host=info[0],
        user=info[1],
        passwd=info[2],
        database=db_name)

    my_cursor = mydb.cursor()

    my_cursor.execute("CREATE TABLE IF NOT EXISTS \
        students (student_id INT AUTO_INCREMENT PRIMARY KEY, \
        first_name VARCHAR(255), last_name VARCHAR(255), \
        father_name VARCHAR(255), email_id VARCHAR(255), \
        age TINYINT(2), age_group VARCHAR(255), \
        gender VARCHAR(255), course VARCHAR(255), \
        medical_com VARCHAR(255), address  VARCHAR(255), \
        phone_no BIGINT(20))")

    my_cursor.close()
    mydb.close()

    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()
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
