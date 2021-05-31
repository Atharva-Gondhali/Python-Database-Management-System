from tkinter import *
from tkinter import ttk

class Widgets:
	def __init__( self, frm ):
		self.frm = frm

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
	
		
		self.ent_age.bind( 
			"<KeyRelease>", lambda event, ent = self.ent_age: inp_num( self, event, ent ) )
		self.ent_phone_number.bind( 
			"<KeyRelease>", lambda event, ent = self.ent_phone_number: inp_num(self,  event, ent ) )
	
		
		self.combo_age_group = ttk.Combobox( 
			self.frm, values = ['U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open'] )
		self.combo_gender = ttk.Combobox( 
			self.frm, values = ['Male', 'Female', 'Other'] )
		self.combo_course = ttk.Combobox( 
			self.frm, values = ['A', 'B', 'C'] )

		
		self.tpl_entry_box = ( self.ent_first_name, self.ent_last_name, self.ent_father_name, 
							   self.ent_email_id, self.ent_age, self.ent_medical_com,
							   self.ent_address, self.ent_phone_number )

		self.tpl_combo_box = ( self.combo_age_group, self.combo_gender, self.combo_course )
		
		self.tpl_lbl = ( self.lbl_first_name, self.lbl_last_name, self.lbl_father_name, 
						 self.lbl_email_id, self.lbl_age, self.lbl_age_group, 
						 self.lbl_gender, self.lbl_course, self.lbl_medical_com, 
						 self.lbl_address, self.lbl_phone_number )

		self.tpl_all_entries = ( self.ent_first_name, self.ent_last_name, self.ent_father_name, 
								 self.ent_email_id, self.ent_age, self.combo_age_group, 
								 self.combo_gender, self.combo_course, self.ent_medical_com, 
								 self.ent_address, self.ent_phone_number )

		self.tpl_all_widgets = self.tpl_all_entries + self.tpl_lbl 

		for i in self.tpl_combo_box:
			i.current(0)