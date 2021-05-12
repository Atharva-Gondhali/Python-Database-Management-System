import mysql.connector

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry( "900x550" )
root.resizable( width = False, height = False )

# mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
# 		passwd = "atharva123@mysql",
# 		database = "project"
#     )

# Check
# print( mydb )

# CREATE A CURSOR
# my_cursor = mydb.cursor()

# CREATE A TABLE (TO BE RUN ONCE)
# my_cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, \
#   first_name VARCHAR(255), \
# 	last_name VARCHAR(255), \
#   email_id VARCHAR(255), \
#   age TINYINT(2), \
#   age_group VARCHAR(255), \
#   gender VARCHAR(255), \
#   course VARCHAR(255), \
#   medical_com VARCHAR(255), \
#   address  VARCHAR(255))")


# FRAMES
frame_menu = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 200, height = 510, padding = 15 )
frame_dash = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 510 )
frame_student = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 510 )

frm_lst = [ frame_menu, frame_dash, frame_student ]
for i in frm_lst:
  i.grid_propagate(0)

frame_menu.grid( row = 0, column = 0, padx = ( 20, 15 ), pady = 20 )      
frame_dash.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )

# STYLES
style = ttk.Style()
style.configure( 'menu.TButton', font = ( 'Helvetica', 10 ), width = 22 )
style.configure( 'heading_text.TButton', font = ( 'Helvetica', 15 ) )

# LABELS

# Label menu
lbl_logo = ttk.Label( frame_menu, text = "logo/app name" )

lbl_logo.grid( row = 5, column = 0, pady = (30, 0) )

# Label students
lbl_student = ttk.Label( frame_student, text = "Student" )

lbl_student.grid( row = 0, column = 0, padx = 10, pady = 10 )

# Label dashboard
lbl_dash = ttk.Label( frame_dash, text = "Dashboard" )

lbl_dash.grid( row = 0, column = 0, padx = 50, pady = 50 )


# FUNCTIONS
def add_std():
  frame_add_std = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 510 )
  frame_add_std.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
  frame_add_std.grid_propagate(0)
  frm_lst.append( frame_add_std )

  lbl_add_std = ttk.Label( frame_add_std, text = "Admit Student", font = ( 'Helvetica', 15 ) )
  lbl_add_std.grid( row = 0, column = 0, padx = 10, pady = 10 )


def open_menu_items( frame ):
  for i in frm_lst:
    if not ( i == frame or i == frame_menu ): 
      i.grid_forget()
      
  frame.grid_propagate(0)
  frame.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )


# BUTTONS 
# Button Styles

# Buttons Menu
btn_dash = ttk.Button( frame_menu, text = "Dashboard", style = 'menu.TButton', command = lambda: open_menu_items( frame_dash ) )
btn_student = ttk.Button( frame_menu, text = "Students", style = 'menu.TButton', command = lambda: open_menu_items( frame_student ) )
btn_unknown1 = ttk.Button( frame_menu, text = ".........", style = 'menu.TButton' )
btn_unknown2 = ttk.Button( frame_menu, text = ".........", style = 'menu.TButton' )
btn_unknown3 = ttk.Button( frame_menu, text = "Settings", style = 'menu.TButton' )

btn_dash.grid( row = 0, column = 0, ipady = 23 )
btn_student.grid( row = 1, column = 0, ipady = 23, pady = ( 10, 0 ) )
btn_unknown1.grid( row = 2, column = 0, ipady = 23, pady = ( 10, 0 ) )
btn_unknown2.grid( row = 3, column = 0, ipady = 23, pady = ( 10, 0 ) )
btn_unknown3.grid( row = 4, column = 0, ipady = 23, pady = ( 10, 0 ) )

# Buttons Dashborad

# Buttons Students
btn_add_std = ttk.Button( frame_student, text = "Admit Student", command = add_std )
btn_edit_std = ttk.Button( frame_student, text = "Edit Student" )

btn_add_std.grid( row = 1, column = 0, padx = 10, pady = 10 )
btn_edit_std.grid( row = 2, column = 0, padx = 10, pady = 10 )


















root.mainloop()