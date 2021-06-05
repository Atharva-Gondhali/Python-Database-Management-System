from tkinter import *
from tkinter import ttk

from Dashboard_front import *
from Student_front import *

class Workspace:
	def __init__( self, win ):
		self.win = win
		self.frm = ttk.Frame( 
			self.win, borderwidth = 3, relief = GROOVE, width = 640, 
			height = 540 )
		self.frm.grid( 
			row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )
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

