import mysql.connector
from pickle import load, dump


def login_db(user):
    db_name = user.lower().replace(" ", "") + "db"
    return db_name


def check_passwd(user, passwd):
    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()

    if acc[user] == passwd:
        return True

    return False


def if_user_exists(user):
    file = open("logger.pkl", "rb")
    acc = load(file)
    file.close()

    if user in acc:
        return True

    return False


def login(user):
    file = open("back_info.pkl", "rb")
    info = load(file)
    info[3] = user
    file.close()

    file = open("back_info.pkl", "wb")
    dump(info, file)
    file.close()


def add_user(user, passwd):
    file = open("back_info.pkl", "rb")
    info = load(file)
    file.close()

    mydb = mysql.connector.connect(
        host=info[0],
        user=info[1],
        passwd=info[2])

    my_cursor = mydb.cursor()
    my_cursor.execute(f"CREATE DATABASE {login_db(user)}")
    my_cursor.close()
    mydb.close()

    mydb = mysql.connector.connect(
        host=info[0],
        user=info[1],
        passwd=info[2],
        database=login_db(user))

    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS \
        students (student_id INT AUTO_INCREMENT PRIMARY KEY, \
        first_name VARCHAR(255), last_name VARCHAR(255), \
        father_name VARCHAR(255), email_id VARCHAR(255), \
        age TINYINT(2), age_group VARCHAR(255), \
        gender VARCHAR(255), course VARCHAR(255), \
        medical_com VARCHAR(255), address  VARCHAR(255), \
        phone_no BIGINT(20))")

    my_cursor.execute("CREATE TABLE IF NOT EXISTS\
        course (course_id INT AUTO_INCREMENT PRIMARY KEY,\
        name VARCHAR(50), description TEXT,\
        duration SMALLINT(4), test1 VARCHAR(50),\
        test2 VARCHAR(50), test3 VARCHAR(50))")

    my_cursor.execute("CREATE TABLE IF NOT EXISTS\
        data (std_id INT AUTO_INCREMENT, FOREIGN KEY (std_id) \
        REFERENCES students (student_id), spt SMALLINT,\
        yt SMALLINT, wt SMALLINT, stt SMALLINT)")

    my_cursor.close()
    mydb.close()

    file = open("logger.pkl", "rb")
    acc = load(file)
    acc.update({user: passwd})
    file.close()

    file = open('logger.pkl', 'wb')
    dump(acc, file)
    file.close()
