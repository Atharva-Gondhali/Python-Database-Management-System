from tkinter import *
from tkinter import ttk

from Student_back import *


class ViewStudent:
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid_propagate(0)
		self.frm.grid( row = 0, column = 0 )

		# FUNCTIONS
		def insert_records( self, condition, value ):
			for i in tree_std.get_children(): 
				tree_std.delete(i)

			result = get_all_std_database( condition, value )

			id = 0
			for i in result:
				tree_std.insert( parent = '', index = 'end', iid = id, text = "", 
					value = ( i[0], i[1], i[2], i[3], i[6], i[8], i[11] ) )
				id += 1

		def set_filter1( self, event ):
			if combo_filter1.get() == 'Age Group': 
				value = [ 'U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open' ]
			elif combo_filter1.get() == 'Course': 
				value = ['A', 'B', 'C']
			elif combo_filter1.get() == 'None': 
				combo_filter2.configure( state = 'disabled' )

				for i in tree_std.get_children(): 
					tree_std.delete(i)

				insert_records( self, '', '' )

			try:
				combo_filter2.configure( values = value, state = 'readonly' )
			except UnboundLocalError:
				pass

		def set_filter2( self, event ):
			if combo_filter1.get() == 'Age Group':
				insert_records( self, 'age_group', combo_filter2.get() )

			elif combo_filter1.get() == 'Course':
				insert_records( self, 'course', combo_filter2.get() )

		def back( self ):
			self.frm.destroy()


		# TREEVIEW	
		tree_std = ttk.Treeview( 
			self.frm, height = 22 )
		tree_std.grid( 
			row = 0, column = 0, columnspan = 3 )

		tree_std['columns'] = ( "ID No.", "First Name", "Last Name",
								"Father's Name", "Age Group", "Course", 
								"Phone No." )
  
		# TREEVIEW - Define columns
		tree_std.column( 
			"#0", width = 0, stretch = NO )
		tree_std.column( 
			"ID No.", width = 50, minwidth = 60, anchor = CENTER )
		tree_std.column( 
			"First Name", width = 95, minwidth = 100, anchor = W )
		tree_std.column( 
			"Last Name", width = 95, minwidth = 100, anchor = W )
		tree_std.column( 
			"Father's Name", width = 120, minwidth = 130, anchor = W )
		tree_std.column( 
			"Age Group", width = 75, minwidth = 80, anchor = CENTER )
		tree_std.column( 
			"Course", width = 80, minwidth = 90, anchor = W )
		tree_std.column( 
			"Phone No.", width = 100, minwidth = 110, anchor = CENTER )

		# TREEVIEW - Define colmn headings
		tree_std.heading( 
			"ID No.", text = "ID No.", anchor = CENTER )
		tree_std.heading( 
			"First Name", text = "First Name", anchor = W )
		tree_std.heading( 
			"Last Name", text = "Last Name", anchor = W )
		tree_std.heading( 
			"Father's Name", text = "Father's Name", anchor = W )
		tree_std.heading( 
			"Age Group", text = "Age Group", anchor = CENTER )
		tree_std.heading( 
			"Course", text = "Course", anchor = W )
		tree_std.heading( 
			"Phone No.", text = "Phone No.", anchor = CENTER )

		# TREEVIEW - Adding records 
		insert_records( self, '', '' )

		# TREEVIEW - Scrollbar
		v_scrollbar = ttk.Scrollbar( self.frm, orient = 'vertical' )
		h_scrollbar = ttk.Scrollbar( self.frm, orient = 'horizontal' )
  
		v_scrollbar.configure( command = tree_std.yview )
		h_scrollbar.configure( command = tree_std.xview )
  
		tree_std.configure( yscrollcommand = v_scrollbar.set,
			xscrollcommand = h_scrollbar.set )

		h_scrollbar.grid( row = 1, column = 0, columnspan = 3, sticky = EW )
		v_scrollbar.grid( row = 0, column = 3, sticky = NS )


		# BUTTONS
		btn_back = ttk.Button( 
			self.frm, text = "Back", command = lambda: back( self ) )
		btn_back.grid( 
			row = 2, column = 2, sticky = E, pady = ( 11, 0 ) )

		# LABELS
		lbl_filter = ttk.Label( 
			self.frm, text = "Filter", font = ( 'Helvetica', 10 ) )
		lbl_filter.grid( 
			row = 2, column = 0, pady = ( 11, 0 ), sticky = E )

		# COMBOBOX
		combo_filter1 = ttk.Combobox( 
			self.frm, values = [ 'None', 'Age Group', 'Course' ], state = 'readonly' )
		combo_filter2 = ttk.Combobox( 
			self.frm, state = 'disabled' )

		combo_filter1.current(0)

		combo_filter1.bind( 
			"<FocusIn>", lambda event: set_filter1( self, event ) )
		combo_filter2.bind( 
			"<FocusIn>", lambda event: set_filter2( self, event ) )

		combo_filter1.grid( 
			row = 2, column = 1, pady = ( 11, 0 ) ) 
		combo_filter2.grid( 
			row = 2, column = 2, pady = ( 11, 0 ), sticky = W ) 