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


def add_course_database(values):
    mydb.connect(database=get_database())
    command = "INSERT INTO course (name, description,\
                duration, test1, test2, test3)\
                VALUES (%s, %s, %s, %s, %s, %s)"

    my_cursor.execute(command, values)
    mydb.commit()