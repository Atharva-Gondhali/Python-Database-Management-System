from pickle import load
import mysql.connector

file = open("back_info.pkl", "rb")
info = load(file)
file.close()

mydb = mysql.connector.connect(
    host=info[0],
    user=info[1],
    passwd=info[2],)

my_cursor = mydb.cursor()

def get_database():
    file = open("back_info.pkl", "rb")
    info = load(file)
    file.close()
    return info[3]

def add_std_database(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11):
    mydb.connect(database = get_database())
    command = "INSERT INTO students (first_name, last_name, father_name, \
			   email_id, age, age_group, gender, course, medical_com, \
			   address, phone_no) \
			   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (f1.get(), f2.get(), f3.get(), f4.get(), f5.get(), f6.get(),
              f7.get(), f8.get(), f9.get(), f10.get(), f11.get())

    my_cursor.execute(command, values)
    mydb.commit()


def get_std_databse(std_id):
    mydb.connect(database = get_database())
    my_cursor.execute(f"SELECT * FROM students WHERE student_id = '{std_id}'")
    std = my_cursor.fetchall()

    return std


def update_std_database(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12):
    mydb.connect(database = get_database())
    my_cursor.execute(f"""UPDATE students SET
		first_name = '{f1.get()}',
		last_name = '{f2.get()}',
		father_name = '{f3.get()}',
		email_id = '{f4.get()}',
		age = '{int(f5.get())}',
		age_group = '{f6.get()}',
		gender = '{f7.get()}',
		course = '{f8.get()}',
		medical_com = '{f9.get()}',
		address = '{f10.get()}',
		phone_no = '{int(f11.get())}'
		WHERE student_id = '{f12.get()}'""")

    mydb.commit()


def get_all_std_database(condition, value):
    mydb.connect(database = get_database())
    if len(condition) == 0:
        my_cursor.execute("SELECT * FROM students")
    else:
        my_cursor.execute(f"SELECT * FROM students \
						   WHERE {condition} = '{value}'")

    result = my_cursor.fetchall()

    return result