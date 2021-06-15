from tkinter import *
from tkinter import ttk

from Main_window import *
from Logger_back import *


class Logger:
	def __init__( self, frm ):
		self.frm = frm
		
		def sign_in():
			if if_user_exists( ent_usenname.get() ):
				if check_passwd( ent_usenname.get(), ent_password.get() ):
					obj = Main( root )
				
				else:
					lbl_inc_pass.configure( foreground = 'black' )
			
			else:
				lbl_inc_user.configure( foreground = 'black' )

		def error_lbl_reset():
			lbl_inc_user.configure( text = "User not found", 
				foreground = "white" )
			lbl_inc_pass.configure( text = "Incorrect Password", 
				foreground = "white" )

		def create_user():
			print( "create user" )
			if len(ent_usenname.get()) > 0:
				if not if_user_exists( ent_usenname.get() ):
					add_user( ent_usenname.get(), ent_password.get() )
					ent_usenname.delete( 0, END )
					ent_password.delete( 0, END )
					error_lbl_reset()
					sign_in_view()
				
				else:
					lbl_inc_user.configure( text = "Username taken", 
						foreground = "black" )

		def sign_up_view():
			error_lbl_reset()
			btn_sign_in.configure( text = "Create User", 
				command = create_user )
			btn_sign_up.configure( text = "Sign In", 
				command = sign_in_view )

		def sign_in_view():
			error_lbl_reset()
			btn_sign_in.configure( text = "Sign In", command = sign_in )
			btn_sign_up.configure( text = "Sign Up", command = sign_up_view )
		

		# LABELS
		lbl_greet = ttk.Label( self.frm, text = "Welcome", 
			font = ("Helvetica", 18) )
		lbl_username = ttk.Label( self.frm, text = "Username:", 
			font = ("Helvetica", 12) )
		lbl_password = ttk.Label( self.frm, text = "Password:", 
			font = ("Helvetica", 12) )
		lbl_or = ttk.Label( self.frm, text = "or", 
			font = ("Helvetica", 10) ) 
		lbl_inc_user = Label( self.frm, text = "User not found", 
			foreground = 'white' ,font = ("Helvetica", 10) )
		lbl_inc_pass = Label( self.frm, text = "Incorrect Password", 
			foreground = 'white' ,font = ("Helvetica", 10) )
		
		lbl_greet.grid( row = 0, column = 0, pady = (0, 25), columnspan = 2 )
		lbl_username.grid( row = 1, column = 0, padx = (0,35), pady = (25, 7) )
		lbl_password.grid( row = 3, column = 0, padx = (0, 35), pady = (7, 7) )
		lbl_or.grid( row = 6, column = 0, columnspan = 2, pady = (5, 5) )
		lbl_inc_user.grid( row = 2, column = 1, sticky = E )
		lbl_inc_pass.grid( row = 4, column = 1, sticky = E )

		
		# ENTRY BOX
		ent_usenname = ttk.Entry( self.frm, width = 28 )
		ent_password = ttk.Entry( self.frm, width = 28 )
		
		ent_usenname.grid( row = 1, column = 1, pady = (20, 0) )
		ent_password.grid( row = 3, column = 1, pady = (5, 0) )
		
		
		# BUTTONS
		btn_sign_in = ttk.Button( self.frm, text = "Sign In", 
			command = sign_in )
		btn_sign_up = ttk.Button( self.frm, text = "Sign Up", 
			command = sign_up_view )
		
		btn_sign_in.grid( row = 5, column = 0, columnspan = 2, pady = (7, 5), 
			sticky = EW )
		btn_sign_up.grid( row = 7, column = 0, columnspan = 2, pady = (5, 0), 
			sticky = EW )


root = Tk()
root.geometry( "438x430" )

main_frame = ttk.Frame( root, borderwidth = 5, relief = GROOVE, padding = 40 )
main_frame.grid( row = 0, column = 0 , padx = 30, pady = 30 )

Logger( main_frame )

root.mainloop()