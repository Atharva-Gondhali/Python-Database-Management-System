from tkinter import *
from tkinter import ttk

from Student_back import *

class Student:
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid_propagate(0)
		self.frm.grid( 
			row = 0, column = 1, padx = ( 5, 20 ), pady = 20 )

		def add_std( self ):
			frame_add_std = ttk.Frame( self.frm, width = 635, height = 535 )
			
			std = AddStudent( frame_add_std )

		# Label students
		lbl_student = ttk.Label( 
			self.frm, text = "Manage Students", font = ( 'Helvetica', 15 ) )
		
		lbl_student.grid( 
			row = 0, column = 0, padx = 30, pady = 15, sticky = W )

		# Buttons Students
		btn_add_std = ttk.Button( 
			self.frm, text = "Admit Student", width = 20, command = lambda: add_std( self ) )
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


class Widgets:
	def __init__( self, frm ):
		self.frm = frm

		self.lbl_first_name = ttk.Label( 
			self.frm, text = "First Name", font = ('Helvetica', 11) )
		self.lbl_last_name = ttk.Label( 
			self.frm, text = "Last Name", font = ('Helvetica', 11) )
		self.lbl_father_name = ttk.Label( 
			self.frm, text = "Father's Name", font = ('Helvetica', 11) )
		self.lbl_email_id = ttk.Label( 
			self.frm, text = "Email ID", font = ('Helvetica', 11) )
		self.lbl_age = ttk.Label( 
			self.frm, text = "Age", font = ('Helvetica', 11) )
		self.lbl_age_group = ttk.Label( 
			self.frm, text = "Age Group", font = ('Helvetica', 11) )
		self.lbl_gender = ttk.Label( 
			self.frm, text = "Gender", font = ('Helvetica', 11) )
		self.lbl_course = ttk.Label( 
			self.frm, text = "Course", font = ('Helvetica', 11) )
		self.lbl_medical_com = ttk.Label( 
			self.frm, text = "Medical Complications", font = ('Helvetica', 11) )
		self.lbl_address = ttk.Label( 
			self.frm, text = "Address", font = ('Helvetica', 11) )
		self.lbl_phone_number = ttk.Label( 
			self.frm, text = "Phone Number", font = ('Helvetica', 11) )

		
		self.ent_first_name = ttk.Entry( 
			self.frm, width = 30 )
		self.ent_last_name = ttk.Entry( 
			self.frm )
		self.ent_father_name = ttk.Entry( 
			self.frm )
		self.ent_email_id = ttk.Entry( 
			self.frm )
		self.ent_age = ttk.Entry( 
			self.frm )
		self.ent_medical_com = ttk.Entry( 
			self.frm )
		self.ent_address = ttk.Entry( 
			self.frm )
		self.ent_phone_number = ttk.Entry( 
			self.frm )
	
		
		# self.ent_age.bind( 
		# 	"<KeyRelease>", lambda event, ent = self.ent_age: inp_num( event, ent ) )
		# self.ent_phone_number.bind( 
		# 	"<KeyRelease>", lambda event, ent = self.ent_phone_number: inp_num( event, ent ) )
	
		
		self.combo_age_group = ttk.Combobox( 
			self.frm, values = ['U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open'] )
		self.combo_gender = ttk.Combobox( 
			self.frm, values = ['Male', 'Female', 'Other'] )
		self.combo_course = ttk.Combobox( 
			self.frm, values = ['A', 'B', 'C'] )

		
		self.lst_entry_box = [ self.ent_first_name, 
							   self.ent_last_name, 
							   self.ent_father_name, 
							   self.ent_email_id, 
							   self.ent_age, 
							   self.ent_medical_com,
							   self.ent_address, 
							   self.ent_phone_number ]

		self.lst_combo_box = [ self.combo_age_group, 
							   self.combo_gender, 
							   self.combo_course ]
		
		self.lst_lbl = [ self.lbl_first_name, 
						 self.lbl_last_name, 
						 self.lbl_father_name, 
						 self.lbl_email_id, 
						 self.lbl_age, 
						 self.lbl_age_group, 
						 self.lbl_gender, 
						 self.lbl_course, 
						 self.lbl_medical_com, 
						 self.lbl_address, 
						 self.lbl_phone_number ]

		self.lst_all_entries = [ self.ent_first_name, 
								 self.ent_last_name, 
								 self.ent_father_name, 
								 self.ent_email_id, 
								 self.ent_age, 
								 self.combo_age_group, 
								 self.combo_gender, 
								 self.combo_course, 
								 self.ent_medical_com, 
								 self.ent_address, 
								 self.ent_phone_number ]

		self.lst_all_widgets = self.lst_all_entries + self.lst_lbl 

		for i in self.lst_combo_box:
			i.current(0)


class AddStudent:
	def __init__( self, frm ):
		self.frm = frm
		self.frm.grid_propagate(0)
		self.frm.grid( 
			row = 0, column = 0 )
		
		# FUNCTIONS
		def add_std( self ):
			add_std_database( self.ent_first_name, 
					 		  self.ent_last_name, 
					 		  self.ent_father_name, 
					 		  self.ent_email_id, 
					 		  self.ent_age, 
					 		  self.combo_age_group, 
					 		  self.combo_gender, 
					 		  self.combo_course, 
					 		  self.ent_medical_com, 
					 		  self.ent_address, 
					 		  self.ent_phone_number )

		# WIDGETS
		wdg = Widgets( self.frm )
		
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

		widgets( wdg )
		
		lbl_add_std = ttk.Label( 
			self.frm, text = "Admit Student", font = ( 'Helvetica', 15 ) )	

		lbl_add_std.grid( 
			row = 0, column = 0, padx = 30, pady = 15, sticky = W )
		
		
		# BUTTONS
		btn_add_std = ttk.Button( 
			self.frm, text = "Add Student", command = lambda: add_std( wdg ) )
		btn_back = ttk.Button( 
			self.frm, text = "Back" )
		btn_clr_field = ttk.Button( 
			self.frm, text = "Clear fields" )

		btn_add_std.grid( 
			row = 12, column = 2, pady = 8, padx = 10, ipadx = 6 )
		btn_back.grid( 
			row = 12, column = 3, pady = 8, padx = 10, ipadx = 6 )
		btn_clr_field.grid( 
			row = 12, column = 1, pady = 8, padx = 10, ipadx = 6, sticky = E )