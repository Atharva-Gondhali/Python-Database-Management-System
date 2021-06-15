from tkinter import ttk

from Dashboard_front import *
from Student_front import *

class Workspace:
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid( row = 1, column = 1, padx = (10, 15), pady = (10, 15) )
		self.frm.grid_propagate(0)

		obj = Dashboard( self.frm )

	def change_dash( self ):
		for widgets in self.frm.winfo_children():
			widgets.destroy()
		Dashboard( self.frm )

	def change_std( self ):
		for widgets in self.frm.winfo_children():
			widgets.destroy()
		Student( self.frm )

