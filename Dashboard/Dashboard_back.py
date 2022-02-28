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


def get_number_std():
    mydb.connect(database=get_database())
    my_cursor.execute("SELECT COUNT(*) FROM students")

    return my_cursor.fetchall()


def get_number_crs():
    mydb.connect(database=get_database())
    my_cursor.execute("SELECT COUNT(*) FROM course")

    return my_cursor.fetchall()


def get_best():
    mydb.connect(database=get_database())
    my_cursor.execute("Select first_name, last_name, spt\
        , yt, wt, stt from students, data where \
        student_id = std_id")
    raw_lst = my_cursor.fetchall()
    def sort(rng):
        lst_total = []
        for i in raw_lst:
            lst_total.append(int(i[2])+int(i[3])+int(i[4])+int(i[5]))
        lst_final = []
        index = 0
        for i in range(rng):
            index = lst_total.index(max(lst_total))
            lst_final.append(str(raw_lst[index][0])+" "+str(raw_lst[index][1]))
            raw_lst.pop(index)
            lst_total.pop(index)
        return lst_final
        

    try:
        return sort(3)
    except ValueError:
        pass
