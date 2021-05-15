# IMPORTS
import mysql.connector

from tkinter import *
from tkinter import ttk

# ********************** REGION MYSQL **********************
# CONNECT TO DATABASE
mydb = mysql.connector.connect( host = "localhost", user = "root", passwd = "atharva123@mysql", database = "project" )


# CREATE A CURSOR
my_cursor = mydb.cursor()
# ******************** REGION MYSQL END ********************


# ********************** REGION TKINTER **********************
# INITIALIZE TKINTER
root = Tk()
root.geometry( "900x580" )
root.resizable( width = False, height = False )


# FUNCTIONS
# Functions Menu -
def open_menu_items( frame ):
  # ********************* REGION START open_menu_items *********************

  for i in frm_lst:
    if not ( i == frame or i == frame_menu ): 
      i.grid_forget()
      
  frame.grid_propagate(0)
  frame.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )

  # ********************** REGION END open_menu_items **********************



# Functions Students -
def add_std():
  # ********************** REGION START add_std **********************

  # FRAME
  frame_add_std = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
  frame_add_std.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
  frame_add_std.grid_propagate(0)
  frm_lst.append( frame_add_std )


  # LABELS
  lbl_add_std = ttk.Label( frame_add_std, text = "Admit Student", font = ( 'Helvetica', 15 ) )
  lbl_first_name = ttk.Label( frame_add_std, text = "First Name", font = ( 'Helvetica', 11 ) )
  lbl_last_name = ttk.Label( frame_add_std, text = "Last Name", font = ( 'Helvetica', 11 ) )
  lbl_father_name = ttk.Label( frame_add_std, text = "Father's Name", font = ( 'Helvetica', 11 ) )
  lbl_email_id = ttk.Label( frame_add_std, text = "Email ID", font = ( 'Helvetica', 11 ) )
  lbl_age = ttk.Label( frame_add_std, text = "Age", font = ( 'Helvetica', 11 ) )
  lbl_age_group = ttk.Label( frame_add_std, text = "Age Group", font = ( 'Helvetica', 11 ) )
  lbl_gender = ttk.Label( frame_add_std, text = "Gender", font = ( 'Helvetica', 11 ) )
  lbl_course = ttk.Label( frame_add_std, text = "Course", font = ( 'Helvetica', 11 ) )
  lbl_medical_com = ttk.Label( frame_add_std, text = "Medical Complications", font = ( 'Helvetica', 11 ) )
  lbl_address = ttk.Label( frame_add_std, text = "Address", font = ( 'Helvetica', 11 ) )
  lbl_phone_number = ttk.Label( frame_add_std, text = "Phone Number", font = ( 'Helvetica', 11 ) )
  
  lbl_add_std.grid( row = 0, column = 0, padx = 30, pady = 15, sticky = W )
  lbl_first_name.grid( row = 1, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_last_name.grid( row = 2, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_father_name.grid( row = 3, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_email_id.grid( row = 4, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_age.grid( row = 5, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_age_group.grid( row = 6, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_gender.grid( row = 7, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_course.grid( row = 8, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_medical_com.grid( row = 9, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_address.grid( row = 10, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
  lbl_phone_number.grid( row = 11, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )


  # ENTRY BOX
  ent_first_name = ttk.Entry( frame_add_std, width = 30 )
  ent_last_name = ttk.Entry( frame_add_std, width = 30 )
  ent_father_name = ttk.Entry( frame_add_std, width = 30 )
  ent_email_id = ttk.Entry( frame_add_std, width = 30 )
  ent_age = ttk.Entry( frame_add_std, width = 30 )
  ent_medical_com = ttk.Entry( frame_add_std, width = 30 )
  ent_address = ttk.Entry( frame_add_std, width = 30 )
  ent_phone_number = ttk.Entry( frame_add_std, width = 30 )
  
  lst_entry_box = [ ent_first_name, ent_last_name, ent_father_name, ent_email_id, ent_age, ent_medical_com,
    ent_address, ent_phone_number ]

  ent_first_name.grid( row = 1, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_last_name.grid( row = 2, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_father_name.grid( row = 3, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_email_id.grid( row = 4, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_age.grid( row = 5, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_medical_com.grid( row = 9, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_address.grid( row = 10, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
  ent_phone_number.grid( row = 11, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )


  # COMBO BOX
  combo_age_group = ttk.Combobox( frame_add_std, values = ['U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open'], width = 27 )
  combo_gender = ttk.Combobox( frame_add_std, values = ['Male', 'Female', 'Other'], width = 27 )
  combo_course = ttk.Combobox( frame_add_std, values = ['A', 'B', 'C'], width = 27 )
  
  lst_combobox = [ combo_age_group, combo_gender, combo_course ]
  for i in lst_combobox:
    i.current(0)

  combo_age_group.grid( row = 6, column = 1, padx = 15, pady = 8, ipady = 1 )
  combo_gender.grid( row = 7, column = 1, padx = 15, pady = 8, ipady = 1 )
  combo_course.grid( row = 8, column = 1, padx = 15, pady = 8, ipady = 1 )


  # INNER FUNCTIONS
  def cancel():
    frame_add_std.grid_remove()

  def clear_fields():
    for i in lst_entry_box:
      i.delete( 0, END )

  def add_std_database():
    command = "INSERT INTO students (first_name, last_name, father_name, email_id, age, age_group, gender, \
      course, medical_com, address, phone_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = ( ent_first_name.get(), ent_last_name.get(), ent_father_name.get(), ent_email_id.get(),
      ent_age.get(), combo_age_group.get(), combo_gender.get(), combo_course.get(), ent_medical_com.get(),
      ent_address.get(), ent_phone_number.get() )

    my_cursor.execute( command, values )
    mydb.commit()
    clear_fields()


  # BUTTONS
  btn_add_std = ttk.Button( frame_add_std, text = "Add Student", command = add_std_database )
  btn_cancel = ttk.Button( frame_add_std, text = "Cancel", command = cancel )
  btn_clr_field = ttk.Button( frame_add_std, text = "Clear fields", command = clear_fields )

  btn_add_std.grid( row = 12, column = 3, pady = 8, padx = 10, ipadx = 6 )
  btn_cancel.grid( row = 12, column = 2, pady = 8, padx = 10, ipadx = 6 )
  btn_clr_field.grid( row = 12, column = 1, pady = 8, padx = 10, ipadx = 6, sticky = E )

  # ********************** REGION END add_std **********************


def view_students():
  # ********************** REGION START view_students **********************

  # FRAME
  frame_view_stds = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
  frame_view_stds.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
  frame_view_stds.grid_propagate(0)
  frm_lst.append( frame_view_stds )


  # TREEVIEW
  tree_std = ttk.Treeview( frame_view_stds, height = 22 )
  tree_std.grid( row = 0, column = 0, columnspan = 3 )

  tree_std['columns'] = ( "ID No.", "First Name", "Last Name", "Father's Name", "Age Group", "Course", "Phone No." )
  
  # TREEVIEW - Define columns
  tree_std.column( "#0", width = 0, stretch = NO )
  tree_std.column( "ID No.", width = 50, minwidth = 60, anchor = CENTER )
  tree_std.column( "First Name", width = 95, minwidth = 100, anchor = W )
  tree_std.column( "Last Name", width = 95, minwidth = 100, anchor = W )
  tree_std.column( "Father's Name", width = 120, minwidth = 130, anchor = W )
  tree_std.column( "Age Group", width = 75, minwidth = 80, anchor = CENTER )
  tree_std.column( "Course", width = 80, minwidth = 90, anchor = W )
  tree_std.column( "Phone No.", width = 100, minwidth = 110, anchor = CENTER )

  # TREEVIEW - Define colmn headings
  tree_std.heading( "ID No.", text = "ID No.", anchor = CENTER )
  tree_std.heading( "First Name", text = "First Name", anchor = W )
  tree_std.heading( "Last Name", text = "Last Name", anchor = W )
  tree_std.heading( "Father's Name", text = "Father's Name", anchor = W )
  tree_std.heading( "Age Group", text = "Age Group", anchor = CENTER )
  tree_std.heading( "Course", text = "Course", anchor = W )
  tree_std.heading( "Phone No.", text = "Phone No.", anchor = CENTER )

  # TREEVIEW - Adding records 
  my_cursor.execute("SELECT * FROM students")
  result = my_cursor.fetchall()

  id = 0
  for i in result:
    tree_std.insert( parent = '', index = 'end', iid = id, text = "", value = ( i[0], i[1], i[2], i[3], i[6], i[8], i[11] ) )
    id += 1

  # TREEVIEW - Scrollbar
  v_scrollbar = ttk.Scrollbar( frame_view_stds, orient = 'vertical' )
  h_scrollbar = ttk.Scrollbar( frame_view_stds, orient = 'horizontal' )
  
  v_scrollbar.configure( command = tree_std.yview )
  h_scrollbar.configure( command = tree_std.xview )
  
  tree_std.configure( yscrollcommand = v_scrollbar.set, xscrollcommand = h_scrollbar.set )

  h_scrollbar.grid( row = 1, column = 0, columnspan = 3, sticky = EW )
  v_scrollbar.grid( row = 0, column = 3, sticky = NS )

  # INNER FUNCTIONS
  def back():
    frame_view_stds.grid_remove()

  def set_filter_lev1( event ):
    if combo_filter1.get() == 'Age Group': 
      value = [ 'U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open' ]
    elif combo_filter1.get() == 'Course': 
      value = ['A', 'B', 'C']
    elif combo_filter1.get() == 'None': 
      combo_filter2.configure( state = 'disabled' )

      for i in tree_std.get_children(): 
        tree_std.delete(i)

      my_cursor.execute("SELECT * FROM students")
      result = my_cursor.fetchall()

      id = 0
      for i in result:
        tree_std.insert( parent = '', index = 'end', iid = id, text = "", value = ( i[0], i[1], i[2], i[3], i[6], i[8], i[11] ) )
        id += 1

    try:
      combo_filter2.configure( values = value, state = 'readonly' )
    except UnboundLocalError:
      pass

  def set_filter_lev2( event ):
    if combo_filter1.get() == 'Age Group':
      value = 'age_group'
    elif combo_filter1.get() == 'Course':
      value = 'course'
    
    my_cursor.execute(f"SELECT * FROM students WHERE {value} = '{combo_filter2.get()}'")
    result = my_cursor.fetchall()

    for i in tree_std.get_children(): 
      tree_std.delete(i)
    
    id = 0
    for i in result:
      tree_std.insert( parent = '', index = 'end', iid = id, text = "", value = ( i[0], i[1], i[2], i[3], i[6], i[8], i[11] ) )
      id += 1
    

  # BUTTONS
  btn_back = ttk.Button( frame_view_stds, text = "Back", command = back )
  btn_back.grid( row = 2, column = 2, sticky = E, pady = ( 11, 0 ) )


  # LABELS
  lbl_filter = ttk.Label( frame_view_stds, text = "Filter", font = ( 'Helvetica', 10 ) )
  lbl_filter.grid( row = 2, column = 0, pady = ( 11, 0 ), sticky = E )


  # COMBOBOX
  combo_filter1 = ttk.Combobox( frame_view_stds, values = [ 'None', 'Age Group', 'Course' ], state = 'readonly' )
  combo_filter2 = ttk.Combobox( frame_view_stds, state = 'disabled')

  combo_filter1.current(0)

  combo_filter1.bind( "<FocusIn>", set_filter_lev1 )
  combo_filter2.bind( "<FocusIn>", set_filter_lev2 )

  combo_filter1.grid( row = 2, column = 1, pady = ( 11, 0 ) ) 
  combo_filter2.grid( row = 2, column = 2, pady = ( 11, 0 ), sticky = W ) 
  
  # ********************** REGION END view_students **********************



# FRAMES
frame_menu = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 200, height = 540, padding = 15 )
frame_dash = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
frame_student = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )

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
lbl_student = ttk.Label( frame_student, text = "Manage Students", font = ( 'Helvetica', 15 ) )
lbl_student.grid( row = 0, column = 0, padx = 30, pady = 15, sticky = W )

# Label dashboard
lbl_dash = ttk.Label( frame_dash, text = "Dashboard", font = ( 'Helvetica', 15 ) )
lbl_dash.grid( row = 0, column = 0, padx = 30, pady = 15, sticky = W )


# BUTTONS 
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
btn_add_std = ttk.Button( frame_student, text = "Admit Student", width = 20, command = add_std )
btn_edit_std = ttk.Button( frame_student, text = "Edit Student", width = 20 )
btn_show_std = ttk.Button( frame_student, text = "View Students", width = 20, command = view_students )

btn_add_std.grid( row = 1, column = 0, padx = 10, pady = 10, ipady = 4 )
btn_edit_std.grid( row = 1, column = 1, padx = 10, pady = 10, ipady = 4 )
btn_show_std.grid( row = 2, column = 0, padx = 10, pady = 10, ipady = 4 )


root.mainloop()

# ********************** REGION TKINTER END **********************