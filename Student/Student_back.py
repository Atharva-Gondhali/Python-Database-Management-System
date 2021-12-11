# IMPORTS
import mysql.connector  # MySQL Connector import
from pickle import load  # Pickle module import

key = {'Search by...': 'first_name', 'First name': 'first_name',
       'Last name': 'last_name', 'Father\'s name': 'father_name',
       'Email id': 'email_id', 'Phone number': 'phone_no',
       'Age Group': 'age_group', 'Course': 'course'}

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
# Internal Functions
def get_database():  # To get user specific database
    file = open("back_info.pkl", "rb")
    info = load(file)
    file.close()

    return info[3]


# External Functions
# Used in EditStudent.py
def get_std_database(std_id):  # To get a student from database
    mydb.connect(database=get_database())  # using student id
    std = get_all_std_database('student_id', std_id)

    return std


# Used in Update.py and View.py
def get_all_std_database(condition='', value=''):  # To get all students
    mydb.connect(database=get_database())

    if len(condition) == 0 and len(value) == 0:  # All students
        my_cursor.execute("SELECT * FROM students")
    elif len(value) == 0 and not len(condition) == 0:  # Specific fields
        my_cursor.execute(f"SELECT student_id,\
                          {condition} FROM students")
    else:  # To get a specific student based on condition
        my_cursor.execute(f"SELECT * FROM students WHERE\
                          {condition} = '{value}'")

    return my_cursor.fetchall()


# Used in AddStudent.py
def add_std_database(values):  # Add Student to database
    mydb.connect(database=get_database())
    command = "INSERT INTO students (first_name, last_name,\
                father_name, email_id, age, age_group, gender,\
                course, medical_com, address, phone_no)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    my_cursor.execute(command, values)
    mydb.commit()


# Used in EditStudent.py
def update_std_database(values):  # Update a student
    mydb.connect(database=get_database())
    my_cursor.execute(f"UPDATE students SET\
        first_name = '{values[0]}',\
        last_name = '{values[1]}',\
        father_name = '{values[2]}',\
        email_id = '{values[3]}',\
        age = '{int(values[4])}',\
        age_group = '{values[5]}',\
        gender = '{values[6]}',\
        course = '{values[7]}',\
        medical_com = '{values[8]}',\
        address = '{values[9]}',\
        phone_no = '{int(values[10])}'\
        WHERE student_id = '{values[11]}'")

    mydb.commit()
