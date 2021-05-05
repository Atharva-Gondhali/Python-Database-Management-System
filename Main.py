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

root.mainloop()