# IMPORTS
import mysql.connector

from tkinter import *
from tkinter import ttk


# **************************** REGION MYSQL START ****************************
# CONNECT TO DATABASE
mydb = mysql.connector.connect( host = "localhost", user = "root", passwd = "atharva123@mysql", database = "project" )


# CREATE A CURSOR
my_cursor = mydb.cursor()
# ***************************** REGION MYSQL END *****************************


# *************************** REGION TKINTER START ***************************
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
def clear_fields():
	for i in lst_entry_box:
		i.delete( 0, END )

def inp_num( event, ent ):
	# ************************* REGION START inp_num *************************
	value = ent.get()	
	ent.delete( 0, END )

	try:
		int( value )
		ent.insert( 0, value )
	except ValueError:
		value_cor = ""
		for i in value:
			if i.isnumeric():
				value_cor += i
		ent.insert( 0, value_cor )
	# ************************** REGION END inp_num **************************

def init_lbls( frm ):
	global lbl_first_name
	global lbl_last_name
	global lbl_father_name
	global lbl_email_id
	global lbl_age
	global lbl_age_group
	global lbl_gender
	global lbl_course
	global lbl_medical_com
	global lbl_address
	global lbl_phone_number

	lbl_first_name = 	ttk.Label( frm, text = "First Name", 			font = ( 'Helvetica', 11 ) )
	lbl_last_name = 	ttk.Label( frm, text = "Last Name", 			font = ( 'Helvetica', 11 ) )
	lbl_father_name = 	ttk.Label( frm, text = "Father's Name", 		font = ( 'Helvetica', 11 ) )
	lbl_email_id = 		ttk.Label( frm, text = "Email ID", 				font = ( 'Helvetica', 11 ) )
	lbl_age = 			ttk.Label( frm, text = "Age", 					font = ( 'Helvetica', 11 ) )
	lbl_age_group = 	ttk.Label( frm, text = "Age Group", 			font = ( 'Helvetica', 11 ) )
	lbl_gender = 		ttk.Label( frm, text = "Gender", 				font = ( 'Helvetica', 11 ) )
	lbl_course = 		ttk.Label( frm, text = "Course", 				font = ( 'Helvetica', 11 ) )
	lbl_medical_com = 	ttk.Label( frm, text = "Medical Complications", font = ( 'Helvetica', 11 ) )
	lbl_address = 		ttk.Label( frm, text = "Address", 				font = ( 'Helvetica', 11 ) )
	lbl_phone_number = 	ttk.Label( frm, text = "Phone Number", 			font = ( 'Helvetica', 11 ) )

def init_ent_combo( frm ):
	global ent_first_name
	global ent_last_name
	global ent_father_name
	global ent_email_id
	global ent_age
	global ent_medical_com
	global ent_address
	global ent_phone_number
	global lst_entry_box

	global combo_age_group
	global combo_gender 
	global combo_course 
	global lst_combobox
	global lst_widgets_entries

	ent_first_name = ttk.Entry( 	frm, width = 30 )
	ent_last_name = ttk.Entry( 		frm )
	ent_father_name = ttk.Entry( 	frm )
	ent_email_id = ttk.Entry( 		frm )
	ent_age = ttk.Entry( 			frm )
	ent_medical_com = ttk.Entry( 	frm )
	ent_address = ttk.Entry( 		frm )
	ent_phone_number = ttk.Entry( 	frm )

	ent_age.bind( 			"<KeyRelease>", lambda event, ent = ent_age: 			inp_num( event, ent ) )
	ent_phone_number.bind( 	"<KeyRelease>", lambda event, ent = ent_phone_number: 	inp_num( event, ent ) )
	
	lst_entry_box = [ ent_first_name, ent_last_name, ent_father_name, ent_email_id, ent_age, ent_medical_com,
		ent_address, ent_phone_number ]

	combo_age_group = ttk.Combobox( frm, values = ['U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open'] )
	combo_gender = ttk.Combobox( 	frm, values = ['Male', 'Female', 'Other'] )
	combo_course = ttk.Combobox( 	frm, values = ['A', 'B', 'C'] )

	lst_widgets_entries = [ ent_first_name, ent_last_name, ent_father_name, ent_email_id, ent_age, 
		combo_age_group, combo_gender, combo_course, ent_medical_com, ent_address, ent_phone_number ]

	lst_combobox = [ combo_age_group, combo_gender, combo_course ]
	for i in lst_combobox:
		i.current(0)

def add_std():
  	# ************************* REGION START add_std *************************
  	# FRAME
	frame_add_std = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
	frame_add_std.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
	frame_add_std.grid_propagate(0)
	frm_lst.append( frame_add_std )

  	# INNER FUNCTIONS
	def cancel():
		frm_lst.remove( frame_add_std )
		frame_add_std.grid_remove()

	def add_std_database():
		command = "INSERT INTO students (first_name, last_name, father_name, email_id, age, age_group, gender, \
			course, medical_com, address, phone_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

		values = ( ent_first_name.get(), ent_last_name.get(), ent_father_name.get(), ent_email_id.get(),
			ent_age.get(), combo_age_group.get(), combo_gender.get(), combo_course.get(), ent_medical_com.get(),
			ent_address.get(), ent_phone_number.get() )

		my_cursor.execute( command, values )
		mydb.commit()
		clear_fields()
	

  	# LABELS
	init_lbls( frame_add_std )
	lbl_add_std = ttk.Label( frame_add_std, text = "Admit Student", font = ( 'Helvetica', 15 ) )

	lbl_add_std.grid( 		row = 0, 	column = 0, padx = 30, 	      pady = 15, 	sticky = W )
	lbl_first_name.grid( 	row = 1, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_last_name.grid( 	row = 2, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_father_name.grid( 	row = 3, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_email_id.grid( 		row = 4, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_age.grid( 			row = 5, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_age_group.grid( 	row = 6, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_gender.grid( 		row = 7, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_course.grid( 		row = 8, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_medical_com.grid( 	row = 9, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_address.grid( 		row = 10, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )
	lbl_phone_number.grid( 	row = 11, 	column = 0, padx = ( 40, 5 ), pady = 8, 	sticky = W )


  	# ENTRY BOX
	init_ent_combo( frame_add_std )

	ent_first_name.grid( 	row = 1, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = E, 	ipady = 1 )
	ent_last_name.grid( 	row = 2, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )
	ent_father_name.grid( 	row = 3, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )
	ent_email_id.grid( 		row = 4, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )
	ent_age.grid( 			row = 5, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )
	ent_medical_com.grid( 	row = 9, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )
	ent_address.grid( 		row = 10, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )
	ent_phone_number.grid( 	row = 11, 	column = 1, 	padx = 15, 	pady = 8, 	sticky = EW, 	ipady = 1 )


	# COMBO BOX
	combo_age_group.grid( 	row = 6, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	combo_gender.grid( 		row = 7, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	combo_course.grid( 		row = 8, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )


	# BUTTONS
	btn_add_std = ttk.Button( 	frame_add_std, text = "Add Student", 	command = add_std_database )
	btn_cancel = ttk.Button( 	frame_add_std, text = "Cancel", 		command = cancel )
	btn_clr_field = ttk.Button( frame_add_std, text = "Clear fields", 	command = clear_fields )

	btn_add_std.grid( 	row = 12, column = 3, pady = 8, padx = 10, ipadx = 6 )
	btn_cancel.grid(	row = 12, column = 2, pady = 8, padx = 10, ipadx = 6 )
	btn_clr_field.grid( row = 12, column = 1, pady = 8, padx = 10, ipadx = 6, sticky = E )
	# ************************** REGION END add_std **************************

def edit_std():
	#************************* REGION START edit_std *************************
	# FRAME
	frame_edit_std = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
	frame_edit_std.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
	frame_edit_std.grid_propagate(0)
	frm_lst.append( frame_edit_std )


	# INNER FUNCTIONS
	def change_state( state ):
		for i in lst_widgets_entries:
			i.configure( state = state )

	def get_std( id ):
		change_state( 'normal' )

		my_cursor.execute( f"SELECT * FROM students WHERE student_id = '{id}'" )
		std = my_cursor.fetchall()
		
		try:
			pos = 1
			for field in lst_widgets_entries:
				field.delete( 0, END )
				field.insert( 0, str( std[0][pos] ) )
				pos += 1
		
		except IndexError:
			change_state( 'disabled' )


  	# LABELS
	init_lbls( frame_edit_std )
	lbl_sel_std = ttk.Label( 	frame_edit_std, text = "Select Student", 		font = ( 'Helvetica', 14 ) )
	lbl_std_id = ttk.Label( 	frame_edit_std, text = "Student's ID No.", 		font = ( 'Helvetica', 11 ) )
	lbl_edit_std = ttk.Label( 	frame_edit_std, text = "Edit Student", 			font = ( 'Helvetica', 14 ) )

	lbl_sel_std.grid( 		row = 0, 	column = 0, padx = 30, 			pady = 15, 	sticky = W )
	lbl_std_id.grid( 		row = 1, 	column = 0, padx = 30, 						sticky = W )
	lbl_edit_std.grid( 		row = 2, 	column = 0, padx = 30, 			pady = 15, 	sticky = W )
	lbl_first_name.grid( 	row = 3, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_last_name.grid( 	row = 4, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_father_name.grid( 	row = 5, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_email_id.grid( 		row = 6, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_age.grid( 			row = 7, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_age_group.grid( 	row = 8, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_gender.grid( 		row = 9, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_course.grid( 		row = 10, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_medical_com.grid( 	row = 11, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_address.grid( 		row = 12, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )
	lbl_phone_number.grid( 	row = 13, 	column = 0, padx = ( 40, 5 ), 	pady = 5, 	sticky = W )


	# ENTRY BOX
	init_ent_combo( frame_edit_std )
	ent_std_id = ttk.Entry( frame_edit_std, width = 30 )
	ent_std_id.bind( '<KeyRelease>', lambda event, ent = ent_std_id: inp_num( event, ent ) )
  
	ent_std_id.grid( 		row = 1, 	column = 1, padx = 15 )
	ent_first_name.grid( 	row = 3, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_last_name.grid( 	row = 4, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_father_name.grid( 	row = 5, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_email_id.grid( 		row = 6, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_age.grid( 			row = 7, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_medical_com.grid( 	row = 11, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_address.grid( 		row = 12, 	column = 1, padx = 15, pady = 5, 	sticky = EW )
	ent_phone_number.grid( 	row = 13, 	column = 1, padx = 15, pady = 5, 	sticky = EW )


	# COMBO BOX
	combo_age_group.grid( 	row = 8, 	column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	combo_gender.grid( 		row = 9, 	column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	combo_course.grid( 		row = 10, 	column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )

	change_state( 'disabled' )

	
	# BUTTONS
	btn_select = ttk.Button( frame_edit_std, text = "Select", width = 15, command = lambda: get_std( ent_std_id.get() ) )
	btn_select.grid( row = 1, column = 2, sticky = W )

  	#************************** REGION END edit_std **************************

def view_std():
  	#************************* REGION START view_std *************************
  	# FRAME
	frame_view_std = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
	frame_view_std.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
	frame_view_std.grid_propagate(0)
	frm_lst.append( frame_view_std )


	# INNER FUNCTIONS
	def back():
		frm_lst.remove( frame_view_std)
		frame_view_std.grid_remove()

	def insert_records( con, value ):
		for i in tree_std.get_children(): 
			tree_std.delete(i)

		if len(con) == 0:
			my_cursor.execute("SELECT * FROM students")
		else:
			my_cursor.execute( f"SELECT * FROM students WHERE {con} = '{value}'" )

		result = my_cursor.fetchall()

		id = 0
		for i in result:
			tree_std.insert( parent = '', index = 'end', iid = id, text = "", value = ( i[0], i[1], i[2], i[3], i[6], i[8], i[11] ) )
			id += 1

	def set_filter_lev1( event ):
		if combo_filter1.get() == 'Age Group': 
			value = [ 'U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open' ]
		elif combo_filter1.get() == 'Course': 
			value = ['A', 'B', 'C']
		elif combo_filter1.get() == 'None': 
			combo_filter2.configure( state = 'disabled' )

			for i in tree_std.get_children(): 
				tree_std.delete(i)

			insert_records( '', '')
      
		try:
			combo_filter2.configure( values = value, state = 'readonly' )
		except UnboundLocalError:
			pass

	def set_filter_lev2( event ):
		if combo_filter1.get() == 'Age Group':
			insert_records( 'age_group', combo_filter2.get() )

		elif combo_filter1.get() == 'Course':
			insert_records( 'course', combo_filter2.get() )


	# TREEVIEW	
	tree_std = ttk.Treeview( frame_view_std, height = 22 )
	tree_std.grid( row = 0, column = 0, columnspan = 3 )

	tree_std['columns'] = ( "ID No.", "First Name", "Last Name", "Father's Name", "Age Group", "Course", "Phone No." )
  
	# TREEVIEW - Define columns
	tree_std.column( "#0", 				width = 0, stretch = NO )
	tree_std.column( "ID No.", 			width = 50, 	minwidth = 60, 	anchor = CENTER )
	tree_std.column( "First Name", 		width = 95, 	minwidth = 100, anchor = W )
	tree_std.column( "Last Name", 		width = 95, 	minwidth = 100, anchor = W )
	tree_std.column( "Father's Name", 	width = 120, 	minwidth = 130, anchor = W )
	tree_std.column( "Age Group", 		width = 75, 	minwidth = 80, 	anchor = CENTER )
	tree_std.column( "Course", 			width = 80, 	minwidth = 90, 	anchor = W )
	tree_std.column( "Phone No.", 		width = 100, 	minwidth = 110, anchor = CENTER )

	# TREEVIEW - Define colmn headings
	tree_std.heading( "ID No.", 		text = "ID No.", 		anchor = CENTER )
	tree_std.heading( "First Name", 	text = "First Name", 	anchor = W )
	tree_std.heading( "Last Name", 		text = "Last Name", 	anchor = W )
	tree_std.heading( "Father's Name", 	text = "Father's Name", anchor = W )
	tree_std.heading( "Age Group", 		text = "Age Group", 	anchor = CENTER )
	tree_std.heading( "Course", 		text = "Course", 		anchor = W )
	tree_std.heading( "Phone No.", 		text = "Phone No.", 	anchor = CENTER )

	# TREEVIEW - Adding records 
	insert_records( '', '' )

	# TREEVIEW - Scrollbar
	v_scrollbar = ttk.Scrollbar( frame_view_std, orient = 'vertical' )
	h_scrollbar = ttk.Scrollbar( frame_view_std, orient = 'horizontal' )
  
	v_scrollbar.configure( command = tree_std.yview )
	h_scrollbar.configure( command = tree_std.xview )
  
	tree_std.configure( yscrollcommand = v_scrollbar.set, xscrollcommand = h_scrollbar.set )

	h_scrollbar.grid( row = 1, column = 0, columnspan = 3, sticky = EW )
	v_scrollbar.grid( row = 0, column = 3, sticky = NS )


	# BUTTONS
	btn_back = ttk.Button( frame_view_std, text = "Back", command = back )
	btn_back.grid( row = 2, column = 2, sticky = E, pady = ( 11, 0 ) )


	# LABELS
	lbl_filter = ttk.Label( frame_view_std, text = "Filter", font = ( 'Helvetica', 10 ) )
	lbl_filter.grid( row = 2, column = 0, pady = ( 11, 0 ), sticky = E )


	# COMBOBOX
	combo_filter1 = ttk.Combobox( frame_view_std, values = [ 'None', 'Age Group', 'Course' ], 	state = 'readonly' )
	combo_filter2 = ttk.Combobox( frame_view_std, 												state = 'disabled' )

	combo_filter1.current(0)

	combo_filter1.bind( "<FocusIn>", set_filter_lev1 )
	combo_filter2.bind( "<FocusIn>", set_filter_lev2 )

	combo_filter1.grid( row = 2, column = 1, pady = ( 11, 0 ) ) 
	combo_filter2.grid( row = 2, column = 2, pady = ( 11, 0 ), sticky = W ) 
  	#************************** REGION END view_std **************************


# FRAMES
frame_menu = ttk.Frame(		root, borderwidth = 3, relief = GROOVE, width = 200, height = 540, padding = 15 )
frame_dash = ttk.Frame( 	root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
frame_student = ttk.Frame( 	root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )

frm_lst = [ frame_menu, frame_dash, frame_student ]
for i in frm_lst: i.grid_propagate(0)

frame_menu.grid( row = 0, column = 0, padx = ( 20, 15 ), 	pady = 20 )      
frame_dash.grid( row = 0, column = 1, padx = ( 5, 20 ), 	pady = 20 )


# STYLES
style = ttk.Style()
style.configure( 'menu.TButton', 			font = ( 'Helvetica', 10 ), width = 22 )
style.configure( 'heading_text.TButton', 	font = ( 'Helvetica', 15 ) ) 


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
btn_dash = ttk.Button( 		frame_menu, text = "Dashboard", style = 'menu.TButton', command = lambda: open_menu_items( frame_dash ) )
btn_student = ttk.Button( 	frame_menu, text = "Students", 	style = 'menu.TButton', command = lambda: open_menu_items( frame_student ) )
btn_unknown1 = ttk.Button( 	frame_menu, text = ".........", style = 'menu.TButton' )
btn_unknown2 = ttk.Button( 	frame_menu, text = ".........", style = 'menu.TButton' )
btn_unknown3 = ttk.Button( 	frame_menu, text = "Settings", 	style = 'menu.TButton' )

btn_dash.grid( 		row = 0, column = 0, ipady = 23 )
btn_student.grid(	row = 1, column = 0, ipady = 23, pady = ( 10, 0 ) )
btn_unknown1.grid( 	row = 2, column = 0, ipady = 23, pady = ( 10, 0 ) )
btn_unknown2.grid( 	row = 3, column = 0, ipady = 23, pady = ( 10, 0 ) )
btn_unknown3.grid( 	row = 4, column = 0, ipady = 23, pady = ( 10, 0 ) )

# Buttons Dashborad

# Buttons Students
btn_add_std = ttk.Button( 	frame_student, text = "Admit Student", 	width = 20, command = add_std )
btn_edit_std = ttk.Button( 	frame_student, text = "Edit Student", 	width = 20, command = edit_std )
btn_view_std = ttk.Button( 	frame_student, text = "View Students", 	width = 20, command = view_std )

btn_add_std.grid( 	row = 1, column = 0, padx = 10, pady = 10, ipady = 4 )
btn_edit_std.grid( 	row = 1, column = 1, padx = 10, pady = 10, ipady = 4 )
btn_view_std.grid( 	row = 2, column = 0, padx = 10, pady = 10, ipady = 4 )

root.mainloop()
# **************************** REGION TKINTER END ****************************