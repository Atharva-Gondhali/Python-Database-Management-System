from tkinter import *
from tkinter import ttk

from Student_back import *
from Student.Widgets import *


class EditStudent:
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid_propagate(0)
		self.frm.grid( row = 0, column = 0 )


		# FUNCTIONS
		def widgets( self ):
			self.lbl_first_name.grid( 
				row = 3, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_last_name.grid( 
				row = 4, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_father_name.grid( 
				row = 5, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_email_id.grid( 
				row = 6, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_age.grid( 
				row = 7, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_age_group.grid( 
				row = 8, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_gender.grid( 
				row = 9, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_course.grid( 
				row = 10, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_medical_com.grid( 
				row = 11, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_address.grid( 
				row = 12, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )
			self.lbl_phone_number.grid( 
				row = 13, column = 0, padx = ( 40, 5 ), pady = 5, sticky = W )

			# ENTRY BOX
			self.ent_first_name.grid( 
				row = 3, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_last_name.grid( 
				row = 4, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_father_name.grid( 
				row = 5, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_email_id.grid( 
				row = 6, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_age.grid( 
				row = 7, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_medical_com.grid( 
				row = 11, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_address.grid( 
				row = 12, column = 1, padx = 15, pady = 5, sticky = EW )
			self.ent_phone_number.grid( 
				row = 13, column = 1, padx = 15, pady = 5, sticky = EW )

			# COMBO BOX
			self.combo_age_group.grid( 
				row = 8, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
			self.combo_gender.grid( 
				row = 9, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )
			self.combo_course.grid( 
				row = 10, column = 1, padx = 15, pady = 8, ipady = 1, sticky = EW )

		def change_state( self, state ):
			for i in self.tpl_all_entries:
				i.configure( state = state )

		def clear_fields( self ):
			for i in self.tpl_entry_box:
				i.delete( 0, END )

			for i in self.tpl_combo_box:
				i.current(0)

		def get_std( self ):
			change_state( self, 'normal' )

			std = get_std_databse( ent_std_id.get() )

			try:
				pos = 1
				for field in self.tpl_all_entries:
					field.delete( 0, END )
					field.insert( 0, str( std[0][pos] ) )
					pos += 1
			except IndexError:
				change_state( self, 'disabled' )

		def update_std( self ):
			update_std_database( self.ent_first_name, self.ent_last_name, 
								 self.ent_father_name, self.ent_email_id, 
								 self.ent_age, self.combo_age_group, 
					 		     self.combo_gender, self.combo_course, 
					 		     self.ent_medical_com, self.ent_address, 
					 		     self.ent_phone_number, ent_std_id )
			
			clear_fields( wdg )
			ent_std_id.delete( 0, END )
			change_state( self, 'disabled' )

		def back( self ):
			self.frm.destroy()

		def callback(P):
			if str.isdigit(P) or P == "":
				return True
			else:
				return False

		# WIDGETS
		wdg = Widgets( self.frm )
		widgets( wdg )
		change_state( wdg, 'disabled' )

		lbl_sel_std = ttk.Label(
			self.frm, text = "Select Student", font = ( 'Helvetica', 14 ) )
		lbl_std_id = ttk.Label( 
			self.frm, text = "Student's ID No.", font = ( 'Helvetica', 11 ) )
		lbl_edit_std = ttk.Label( 
			self.frm, text = "Edit Student", font = ( 'Helvetica', 14 ) )

		lbl_sel_std.grid( 
			row = 0, column = 0, padx = 30, pady = 15, sticky = W )
		lbl_std_id.grid( 
			row = 1, column = 0, padx = 30, sticky = W )
		lbl_edit_std.grid( 
			row = 2, column = 0, padx = 30, pady = 15, sticky = W )


		# ENTRY BOX
		vcmd = ( self.frm.register( callback ) )
		
		ent_std_id = ttk.Entry( 
			self.frm, width = 30, validate = 'all', 
			validatecommand = ( vcmd, '%P' ) )
		
		ent_std_id.grid( 
			row = 1, column = 1, padx = 15 )
		

		# BUTTONS
		btn_select = ttk.Button( 
			self.frm, text = "Select", width = 15, 
			command = lambda: get_std( wdg ) )
		btn_update = ttk.Button( 
			self.frm, text = "Update", width = 13, 
			command = lambda: update_std( wdg ) )
		btn_back = ttk.Button( 
			self.frm, text = "Back", width = 13, 
			command = lambda: back( self ) )
		
		btn_select.grid( 
			row = 1, column = 2, sticky = W )
		btn_update.grid( 
			row = 14, column = 2, padx = 10 )
		btn_back.grid( 
			row = 14, column = 3, padx = 10 )