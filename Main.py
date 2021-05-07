import mysql.connector

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry( "400x600" )


mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
		passwd = "atharva123@mysql",
		database = "project"
    )

# Check
# print( mydb )

# CREATE A CURSOR
my_cursor = mydb.cursor()

# CREATE A TABLE (TO BE RUN ONCE)
my_cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, \
  first_name VARCHAR(255), \
	last_name VARCHAR(255), \
  email_id VARCHAR(255), \
  age TINYINT(2), \
  age_group VARCHAR(255), \
  gender VARCHAR(255), \
  course VARCHAR(255), \
  medical_com VARCHAR(255), \
  address  VARCHAR(255))")


root.mainloop()