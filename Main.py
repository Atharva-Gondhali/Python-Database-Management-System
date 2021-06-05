# IMPORTS
import mysql.connector

from tkinter import *
from tkinter import ttk

from Main_menu import *

root = Tk()

class Main:
	def __init__( self, win ):
		self.win = win
		self.win.geometry( "900x580" )
		self.win.resizable( width = False, height = False )

		Menu( self.win )


obj = Main( root )
root.mainloop()