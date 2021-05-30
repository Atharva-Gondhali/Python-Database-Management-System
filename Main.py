# IMPORTS
import mysql.connector

from tkinter import *
from tkinter import ttk

from Student_front import *
from Dashboard_front import *

# *************************** REGION TKINTER START ***************************
# INITIALIZE TKINTER
root = Tk()


class Main():
	def __init__( self, win ):
		self.win = win
		self.win.geometry( "900x580" )
		self.win.resizable( width = False, height = False )


		# Functions Menu -
		def open_menu_items( frame ):
  			# ********************* REGION START open_menu_items *********************
			for widgets in frame_secondary.winfo_children():
				widgets.destroy()

			if frame == "Dashboard": 
				frm = Dashboard( frame_secondary )
  	
			elif frame == "Student": 
				frm = Student( frame_secondary )

		# FRAMES
		frame_menu = ttk.Frame(	
			self.win, borderwidth = 3, relief = GROOVE, width = 200, height = 540, padding = 15 )
		frame_secondary = ttk.Frame( 
			self.win, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )

		frame_menu.grid(
			row = 0, column = 0, padx = ( 20, 15 ), pady = 20 )
		
		frame_menu.grid_propagate(0)

		frm = Dashboard( frame_secondary )

		# STYLES
		style = ttk.Style()
		style.configure( 'menu.TButton', font = ( 'Helvetica', 10 ), width = 22 )
		style.configure( 'heading_text.TButton', font = ( 'Helvetica', 15 ) ) 

		# Buttons Menu
		btn_dash = ttk.Button( 
			frame_menu, text = "Dashboard", style = 'menu.TButton', command = lambda: open_menu_items( "Dashboard" ) )
		btn_student = ttk.Button( 
			frame_menu, text = "Students", style = 'menu.TButton', command = lambda: open_menu_items( "Student" ) )
		btn_unknown1 = ttk.Button( 
			frame_menu, text = ".........", style = 'menu.TButton' )
		btn_unknown2 = ttk.Button( 
			frame_menu, text = ".........", style = 'menu.TButton' )
		btn_unknown3 = ttk.Button( 
			frame_menu, text = "Settings", style = 'menu.TButton' )

		btn_dash.grid( 	
			row = 0, column = 0, ipady = 23 )
		btn_student.grid( 
			row = 1, column = 0, ipady = 23, pady = ( 10, 0 ) )
		btn_unknown1.grid( 
			row = 2, column = 0, ipady = 23, pady = ( 10, 0 ) )
		btn_unknown2.grid( 
			row = 3, column = 0, ipady = 23, pady = ( 10, 0 ) )
		btn_unknown3.grid( 
			row = 4, column = 0, ipady = 23, pady = ( 10, 0 ) )

		# Label menu
		lbl_logo = ttk.Label( 
			frame_menu, text = "logo/app name" )
		
		lbl_logo.grid( 
			row = 5, column = 0, pady = (30, 0) )


# FUNCTIONS
def back( frm ):
	for widgets in lst_widgets_all:
		widgets.destroy()

	frm_lst.remove( frm)
	frm.grid_remove()

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

	def update_std():
		my_cursor.execute(f"""UPDATE students SET
			first_name = '{ent_first_name.get()}',
			last_name = '{ent_last_name.get()}',
			father_name = '{ent_father_name.get()}',
			email_id = '{ent_email_id.get()}',
			age = '{int( ent_age.get() )}',
			age_group = '{combo_age_group.get()}',
			gender = '{combo_gender.get()}',
			course = '{combo_course.get()}',
			medical_com = '{ent_medical_com.get()}',
			address = '{ent_address.get()}',
			phone_no = '{int(ent_phone_number.get() )}'
			WHERE student_id = '{ent_std_id.get()}'""") 

		mydb.commit()
		
		clear_fields()
		ent_std_id.delete( 0, END )
		change_state( 'disabled' )

	def get_std():
		change_state( 'normal' )

		my_cursor.execute( f"SELECT * FROM students WHERE student_id = '{ent_std_id.get()}'" )
		std = my_cursor.fetchall()
		
		try:
			pos = 1
			for field in lst_widgets_entries:
				field.delete( 0, END )
				field.insert( 0, str( std[0][pos] ) )
				pos += 1
		except IndexError:
			change_state( 'disabled' )

	init_widgets( frame_edit_std )
  	
  	# LABELS
	lbl_sel_std = ttk.Label( frame_edit_std, text = "Select Student", font = ( 'Helvetica', 14 ) )
	lbl_std_id = ttk.Label( frame_edit_std, text = "Student's ID No.", font = ( 'Helvetica', 11 ) )
	lbl_edit_std = ttk.Label( frame_edit_std, text = "Edit Student", font = ( 'Helvetica', 14 ) )

	lbl_sel_std.grid( row = 0, column = 0, padx = 30, pady = 15, sticky = W )
	lbl_std_id.grid( row = 1, column = 0, padx = 30, sticky = W )
	lbl_edit_std.grid( row = 2, column = 0, padx = 30, pady = 15, sticky = W )
	lbl_first_name.grid( row = 3, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_last_name.grid( row = 4, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_father_name.grid( row = 5, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_email_id.grid( row = 6, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_age.grid( row = 7, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_age_group.grid( row = 8, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_gender.grid( row = 9, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_course.grid( row = 10, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_medical_com.grid( row = 11, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_address.grid( row = 12, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
	lbl_phone_number.grid( row = 13, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )

	# ENTRY BOX
	ent_std_id = ttk.Entry( frame_edit_std, width = 30 )
	ent_std_id.bind( '<KeyRelease>', lambda event, ent = ent_std_id: inp_num( event, ent ) )
  
	ent_std_id.grid( row = 1, column = 1, padx = 15 )
	ent_first_name.grid( row = 3, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_last_name.grid( row = 4, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_father_name.grid( row = 5, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_email_id.grid( row = 6, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_age.grid( row = 7, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_medical_com.grid( row = 11, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_address.grid( row = 12, column = 1, padx = 15, pady = 5, sticky = EW )
	ent_phone_number.grid( row = 13, column = 1, padx = 15, pady = 5, sticky = EW )

	# COMBO BOX
	combo_age_group.grid( row = 8, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	combo_gender.grid( row = 9, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	combo_course.grid( row = 10, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
	change_state( 'disabled' )

	# BUTTONS
	btn_select = ttk.Button( frame_edit_std, text = "Select", width = 15, command = get_std )
	btn_update = ttk.Button( frame_edit_std, text = "Update", width = 13, command = update_std )
	btn_back = ttk.Button( frame_edit_std, text = "Back", width = 13, command = lambda: back( frame_edit_std ) )
	
	btn_select.grid( row = 1, column = 2, sticky = W )
	btn_update.grid( row = 14, column = 2, padx = 10 )
	btn_back.grid( row = 14, column = 3, padx = 10 )

  	#************************** REGION END edit_std **************************

def view_std():
  	#************************* REGION START view_std *************************
  	# FRAME
	frame_view_std = ttk.Frame( root, borderwidth = 3, relief = GROOVE, width = 640, height = 540 )
	frame_view_std.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
	frame_view_std.grid_propagate(0)
	frm_lst.append( frame_view_std )

	# INNER FUNCTIONS
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
	btn_back = ttk.Button( frame_view_std, text = "Back", command = lambda: back( frame_view_std ) )
	btn_back.grid( row = 2, column = 2, sticky = E, pady = ( 11, 0 ) )

	# LABELS
	lbl_filter = ttk.Label( frame_view_std, text = "Filter", font = ( 'Helvetica', 10 ) )
	lbl_filter.grid( row = 2, column = 0, pady = ( 11, 0 ), sticky = E )

	# COMBOBOX
	combo_filter1 = ttk.Combobox( frame_view_std, values = [ 'None', 'Age Group', 'Course' ], state = 'readonly' )
	combo_filter2 = ttk.Combobox( frame_view_std, state = 'disabled' )

	combo_filter1.current(0)

	combo_filter1.bind( "<FocusIn>", set_filter_lev1 )
	combo_filter2.bind( "<FocusIn>", set_filter_lev2 )

	combo_filter1.grid( row = 2, column = 1, pady = ( 11, 0 ) ) 
	combo_filter2.grid( row = 2, column = 2, pady = ( 11, 0 ), sticky = W ) 
  	#************************** REGION END view_std **************************


obj = Main( root )
root.mainloop()
# **************************** REGION TKINTER END ****************************