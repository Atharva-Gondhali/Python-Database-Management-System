# IMPORTS
from tkinter import ttk

from Main_menu import *

root = Tk()

class Main:
	def __init__( self, win ):
		self.win = win
		self.win.geometry( "915x680" )
		self.win.resizable( width = False, height = False )

		main_frame = ttk.Frame( self.win, borderwidth = 3, relief = GROOVE,
			width = 895, height = 600 )
		main_frame.grid_propagate(0)
		main_frame.grid( row = 0, column = 0, padx = 10, pady = 10 )

		menu_frame = ttk.Frame( main_frame, borderwidth = 3, relief = GROOVE, 
			width = 200, height = 540, padding = 15 )

		workspace_frame = ttk.Frame( main_frame, borderwidth = 3, 
			relief = GROOVE, width = 640, height = 540 )

		Menu( menu_frame, workspace_frame )


obj = Main( root )
root.mainloop()