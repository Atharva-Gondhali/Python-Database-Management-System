from tkinter import ttk

from Student.AddStudent import *
from Student.EditStudent import	*
from Student.ViewStudent import *

# Classes
class Student:
	def __init__( self, frm ):
		self.frm = frm

		def add_std( self ):
			frame_add_std = ttk.Frame( self.frm, width = 635, height = 535 )
			
			std = AddStudent( frame_add_std )

		def edit_std( self ):
			frame_edit_std = ttk.Frame( self.frm, width = 635, height = 535 )

			std = EditStudent( frame_edit_std )

		def view_std( self ):
			frame_view_std = ttk.Frame( self.frm, width = 635, height = 535 )

			std = ViewStudent( frame_view_std )

		# Label students
		lbl_student = ttk.Label( self.frm, text = "Manage Students", 
			font = ('Helvetica', 15) )
		
		lbl_student.grid( row = 0, column = 0, padx = 30, pady = 15, 
			sticky = W )

		# Buttons Students
		btn_add_std = ttk.Button( self.frm, text = "Admit Student", 
			width = 20, command = lambda: add_std( self ) )
		btn_edit_std = ttk.Button( self.frm, text = "Edit Student", 
			width = 20, command = lambda: edit_std( self ) )
		btn_view_std = ttk.Button( self.frm, text = "View Students", 
			width = 20, command = lambda: view_std( self ) )
		
		btn_add_std.grid( row = 1, column = 0, padx = 10, pady = 10, 
			ipady = 4 )
		btn_edit_std.grid( row = 1, column = 1, padx = 10, pady = 10, 
			ipady = 4 )
		btn_view_std.grid( row = 2, column = 0, padx = 10, pady = 10, 
			ipady = 4 )