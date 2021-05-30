
class variables:
	def __init__( self ):
		self.a = 10
		self.b = 10
		self.add = 0

	def add(self):
		self.add = self.a + self.b

class calculate:
	def display(self):
		print( self.add )


obj = variables()	
obj.add()
calculate.display( obj )

#Class1 
# class Test: 
#     def __init__(self): 
#         self.a = 10 
#         self.b = 20 
#         self.add = 0 
 
#     def calc(self): 
#         self.add = self.a+self.b 
 
# #Class 2 
# class Test2: 
#     def display(self): 
#         print('adding of two numbers: ',self.add) 
# #creating object for Class1 
# obj = Test() 
# #invoking calc method() 
# obj.calc() 
# #passing class1 object to class2 
# Test2.display(obj) 






def init_widgets( frm ):
	# global lbl_first_name
	# global lbl_last_name
	# global lbl_father_name
	# global lbl_email_id
	# global lbl_age
	# global lbl_age_group
	# global lbl_gender
	# global lbl_course
	# global lbl_medical_com
	# global lbl_address
	# global lbl_phone_number
	
	# global ent_first_name
	# global ent_last_name
	# global ent_father_name
	# global ent_email_id
	# global ent_age
	# global ent_medical_com
	# global ent_address
	# global ent_phone_number

	# global combo_age_group
	# global combo_gender 
	# global combo_course 
	
	# global lst_entry_box
	# global lst_combobox
	# global lst_widgets_entries
	# global lst_widgets_all

	# lbl_first_name = ttk.Label( frm, text = "First Name", font = ( 'Helvetica', 11 ) )
	# lbl_last_name = ttk.Label( frm, text = "Last Name", font = ( 'Helvetica', 11 ) )
	# lbl_father_name = ttk.Label( frm, text = "Father's Name", font = ( 'Helvetica', 11 ) )
	# lbl_email_id = ttk.Label( frm, text = "Email ID", font = ( 'Helvetica', 11 ) )
	# lbl_age = ttk.Label( frm, text = "Age", font = ( 'Helvetica', 11 ) )
	# lbl_age_group = ttk.Label( frm, text = "Age Group", font = ( 'Helvetica', 11 ) )
	# lbl_gender = ttk.Label( frm, text = "Gender", font = ( 'Helvetica', 11 ) )
	# lbl_course = ttk.Label( frm, text = "Course", font = ( 'Helvetica', 11 ) )
	# lbl_medical_com = ttk.Label( frm, text = "Medical Complications", font = ( 'Helvetica', 11 ) )
	# lbl_address = ttk.Label( frm, text = "Address", font = ( 'Helvetica', 11 ) )
	# lbl_phone_number = ttk.Label( frm, text = "Phone Number", font = ( 'Helvetica', 11 ) )

	# ent_first_name = ttk.Entry( frm, width = 30 )
	# ent_last_name = ttk.Entry( frm )
	# ent_father_name = ttk.Entry( frm )
	# ent_email_id = ttk.Entry( frm )
	# ent_age = ttk.Entry( frm )
	# ent_medical_com = ttk.Entry( frm )
	# ent_address = ttk.Entry( frm )
	# ent_phone_number = ttk.Entry( frm )

	# ent_age.bind( "<KeyRelease>", lambda event, ent = ent_age: inp_num( event, ent ) )
	# ent_phone_number.bind( "<KeyRelease>", lambda event, ent = ent_phone_number: inp_num( event, ent ) )
	
	# combo_age_group = ttk.Combobox( frm, values = ['U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open'] )
	# combo_gender = ttk.Combobox( frm, values = ['Male', 'Female', 'Other'] )
	# combo_course = ttk.Combobox( frm, values = ['A', 'B', 'C'] )

	# lst_entry_box = [ ent_first_name, ent_last_name, ent_father_name, ent_email_id, ent_age, ent_medical_com,
	# 	ent_address, ent_phone_number ]

	# lst_combobox = [ combo_age_group, combo_gender, combo_course ]
	# for i in lst_combobox:
	# 	i.current(0)

	# lst_widgets_entries = [ ent_first_name, ent_last_name, ent_father_name, ent_email_id, ent_age, 
	# 	combo_age_group, combo_gender, combo_course, ent_medical_com, ent_address, ent_phone_number ]

	# lst_widgets_all = lst_widgets_entries + [lbl_first_name, lbl_last_name, lbl_father_name, lbl_email_id, lbl_age,
	# 	lbl_age_group, lbl_gender, lbl_course, lbl_medical_com, 
	# 	lbl_address, lbl_phone_number ]

