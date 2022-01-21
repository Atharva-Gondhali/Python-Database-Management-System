import mysql.connector  # MySQL Connector import
from pickle import load  # Pickle module import

# Extracting database login b_info from pickle b_file
b_file = open("back_info.pkl", "rb")
b_info = load(b_file)
b_file.close()

# Connecting to Database
mydb = mysql.connector.connect(
    host=b_info[0],
    user=b_info[1],
    passwd=b_info[2], )
# Initializing database cursor
my_cursor = mydb.cursor()


# FUNCTIONS
def get_database():  # To get user specific database
    file = open("back_info.pkl", "rb")
    info = load(file)
    file.close()

    return info[3]


def get_course_names():
    mydb.connect(database=get_database())
    my_cursor.execute("SELECT course_id, name FROM course")

    return my_cursor.fetchall()


# Used in CreateCourse.py
def add_course_database(values):
    mydb.connect(database=get_database())
    command = "INSERT INTO course (name, description,\
                duration, test1, test2, test3)\
                VALUES (%s, %s, %s, %s, %s, %s)"

    my_cursor.execute(command, values)
    mydb.commit()


def get_update_course(course_id):
    mydb.connect(database=get_database())

    my_cursor.execute(f"SELECT * FROM course WHERE\
                      course_id = '{course_id}'")
    return tuple(my_cursor.fetchall())

def update_course_database(values):
    mydb.connect(database=get_database())
    my_cursor.execute(f"UPDATE course SET\
        name = '{values[0]}',\
        description = '{values[1]}',\
        duration = '{int(values[2])}',\
        test1 = '{values[3]}',\
        test2 = '{values[4]}',\
        test3 = '{values[5]}'\
        WHERE course_id = '{values[6]}'")

    mydb.commit()

# Used in ViewCourses.py
def get_all_courses():
    mydb.connect(database=get_database())

    my_cursor.execute("SELECT * FROM course")

    return my_cursor.fetchall()
