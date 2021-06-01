# IMPORTS
import mysql.connector

from tkinter import *
from tkinter import ttk

from Student_front import *
from Dashboard_front import *


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