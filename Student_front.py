from tkinter import *
from tkinter import ttk

from Student_back import *

class Student():
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid_propagate(0)
		self.frm.grid( row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )


		# Buttons Students
		btn_add_std = ttk.Button( 
			self.frm, text = "Admit Student", width = 20 )
		btn_edit_std = ttk.Button( 
			self.frm, text = "Edit Student", width = 20 )
		btn_view_std = ttk.Button( 
			self.frm, text = "View Students", width = 20 )
		
		btn_add_std.grid( 
			row = 1, column = 0, padx = 10, pady = 10, ipady = 4 )
		btn_edit_std.grid( 
			row = 1, column = 1, padx = 10, pady = 10, ipady = 4 )
		btn_view_std.grid( 
			row = 2, column = 0, padx = 10, pady = 10, ipady = 4 )