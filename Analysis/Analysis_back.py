# IMPORTS
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

def get_std_by_id(id):
    mydb.connect(database=get_database())
    my_cursor.execute(f"SELECT first_name, last_name,\
        course, age_group, spt, yt, wt, stt FROM\
        students, data WHERE student_id = {id} \
        AND std_id = {id}")

    return my_cursor.fetchall()

def update(id, values):
    mydb.connect(database=get_database())
    my_cursor.execute(f"UPDATE data SET spt = {int(values[0])},\
        yt = {int(values[1])}, wt = {int(values[2])},\
        stt = {int(values[3])} WHERE std_id = '{id}'")

    mydb.commit()
