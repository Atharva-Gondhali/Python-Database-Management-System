# IMPORTS
import mysql.connector

from tkinter import *
from tkinter import ttk

from Student_front import *
from Dashboard_front import *

# *************************** REGION TKINTER START ***************************
# INITIALIZE TKINTER
root = Tk()


class Main:
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


obj = Main( root )
root.mainloop()



# FUNCTIONS
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


# **************************** REGION TKINTER END ****************************