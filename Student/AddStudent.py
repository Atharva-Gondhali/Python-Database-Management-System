from tkinter import *
from tkinter import ttk

from Student_back import *
from Student.Widgets import *

class AddStudent:
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid_propagate(0)
		self.frm.grid( 
			row = 0, column = 0 )

		# FUNCTIONS
		def widgets( self ):
			self.lbl_first_name.grid( 
				row = 1, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_last_name.grid(
			 row = 2, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_father_name.grid( 
				row = 3, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_email_id.grid( 
				row = 4, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_age.grid( 
				row = 5, 	column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_age_group.grid( 
				row = 6, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_gender.grid( 
				row = 7, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_course.grid( 
				row = 8, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_medical_com.grid( 
				row = 9, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_address.grid( 
				row = 10, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )
			self.lbl_phone_number.grid( 
				row = 11, column = 0, padx = ( 40, 5 ), pady = 8, sticky = W )	

			# ENTRY BOX
			self.ent_first_name.grid( 
				row = 1, column = 1, padx = 15, pady = 8, sticky = E, ipady = 1 )
			self.ent_last_name.grid( 
				row = 2, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )
			self.ent_father_name.grid( 
				row = 3, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )
			self.ent_email_id.grid( 
				row = 4, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )
			self.ent_age.grid( 
				row = 5, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )
			self.ent_medical_com.grid( 
				row = 9, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )
			self.ent_address.grid( 
				row = 10, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )
			self.ent_phone_number.grid( 
				row = 11, column = 1, padx = 15, pady = 8, sticky = EW, ipady = 1 )

			# COMBO BOX
			self.combo_age_group.grid( 
				row = 6, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
			self.combo_gender.grid( 
				row = 7, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
			self.combo_course.grid( 
				row = 8, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )

		def add_std( self ):
			add_std_database( self.ent_first_name, self.ent_last_name, 
							  self.ent_father_name, self.ent_email_id, 
							  self.ent_age, self.combo_age_group, 
					 		  self.combo_gender, self.combo_course, 
					 		  self.ent_medical_com, self.ent_address, 
					 		  self.ent_phone_number )

		def clear_fields( self ):
			for i in self.tpl_entry_box:
				i.delete( 0, END )

			for i in self.tpl_combo_box:
				i.current(0)	

		def inp_num( self, event, ent ):
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

		def back( self ):
			self.frm.destroy() 	


		# WIDGETS
		wdg = Widgets( self.frm )
		widgets( wdg )

		lbl_add_std = ttk.Label( 
			self.frm, text = "Admit Student", font = ( 'Helvetica', 15 ) )	

		lbl_add_std.grid( 
			row = 0, column = 0, padx = 30, pady = 15, sticky = W )


		# BUTTONS
		btn_add_std = ttk.Button( 
			self.frm, text = "Add Student", command = lambda: add_std( wdg ) )
		btn_back = ttk.Button( 
			self.frm, text = "Back", command = lambda: back( self ) )
		btn_clr_field = ttk.Button( 
			self.frm, text = "Clear fields", command = lambda: clear_fields( wdg ) )

		btn_add_std.grid( 
			row = 12, column = 2, pady = 8, padx = 10, ipadx = 6 )
		btn_back.grid( 
			row = 12, column = 3, pady = 8, padx = 10, ipadx = 6 )
		btn_clr_field.grid( 
			row = 12, column = 1, pady = 8, padx = 10, ipadx = 6, sticky = E )