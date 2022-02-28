from tkinter import Text, END
from tkinter import ttk  # Tkinter Imports
from Course.Course_back import get_course_names


class StudentWidgets:
    def __init__(self, frm):  # initializing frame and class
        self.frm = frm

        def callback(P):  # To validate some entry box to an integer input
            if str.isdigit(P) or P == "":
                return True
            else:
                return False

        # WIDGETS
        # Widget - Labels
        # Defining
        self.lbl_first_name = ttk.Label(self.frm, text="First Name",
                                        font=('Helvetica', 11))
        self.lbl_last_name = ttk.Label(self.frm, text="Last Name",
                                       font=('Helvetica', 11))
        self.lbl_father_name = ttk.Label(self.frm, text="Father's Name",
                                         font=('Helvetica', 11))
        self.lbl_email_id = ttk.Label(self.frm, text="Email ID",
                                      font=('Helvetica', 11))
        self.lbl_age = ttk.Label(self.frm, text="Age",
                                 font=('Helvetica', 11))
        self.lbl_age_group = ttk.Label(self.frm, text="Age Group",
                                       font=('Helvetica', 11))
        self.lbl_gender = ttk.Label(self.frm, text="Gender",
                                    font=('Helvetica', 11))
        self.lbl_course = ttk.Label(self.frm, text="Course",
                                    font=('Helvetica', 11))
        self.lbl_medical_com = ttk.Label(self.frm, text="Medical Complications",
                                         font=('Helvetica', 11))
        self.lbl_address = ttk.Label(self.frm, text="Address",
                                     font=('Helvetica', 11))
        self.lbl_phone_number = ttk.Label(self.frm, text="Phone Number",
                                          font=('Helvetica', 11))

        v_cmd = (self.frm.register(callback))  # Validating input

        # Widget - Entry box
        # Defining
        self.ent_first_name = ttk.Entry(self.frm, width=30)
        self.ent_last_name = ttk.Entry(self.frm)
        self.ent_father_name = ttk.Entry(self.frm)
        self.ent_email_id = ttk.Entry(self.frm)
        self.ent_age = ttk.Entry(self.frm, validate='all',
                                 validatecommand=(v_cmd, '%P'))
        self.ent_medical_com = ttk.Entry(self.frm)
        self.ent_address = ttk.Entry(self.frm)
        self.ent_phone_number = ttk.Entry(self.frm, validate='all',
                                          validatecommand=(v_cmd, '%P'))

        # Widget - Combo box
        # Defining
        courses_r = get_course_names()
        courses_s = ()
        for i in courses_r:
            courses_s += (f"{i[1]} ({i[0]})", )
        self.combo_age_group = ttk.Combobox(self.frm, state='readonly',
                                            values=('U-12', 'U-14', 'U-16',
                                                    'U-18', 'U-25', 'Open'))
        self.combo_gender = ttk.Combobox(self.frm, state='readonly',
                                         values=('Male', 'Female', 'Other'))
        self.combo_course = ttk.Combobox(self.frm, state='readonly',
                                         values=courses_s)

        # Variables
        # Tuples of widgets
        self.tpl_entry_box = (self.ent_first_name, self.ent_last_name,
                              self.ent_father_name, self.ent_email_id,
                              self.ent_age, self.ent_medical_com,
                              self.ent_address, self.ent_phone_number)

        self.tpl_combo_box = (self.combo_age_group, self.combo_gender,
                              self.combo_course)

        self.tpl_lbl = (self.lbl_first_name, self.lbl_last_name,
                        self.lbl_father_name, self.lbl_email_id,
                        self.lbl_age, self.lbl_age_group,
                        self.lbl_gender, self.lbl_course,
                        self.lbl_medical_com, self.lbl_address,
                        self.lbl_phone_number)

        self.tpl_all_entries = (self.ent_first_name, self.ent_last_name,
                                self.ent_father_name, self.ent_email_id,
                                self.ent_age, self.combo_age_group,
                                self.combo_gender, self.combo_course,
                                self.ent_medical_com, self.ent_address,
                                self.ent_phone_number)

        self.tpl_all_widgets = self.tpl_all_entries + self.tpl_lbl

        # Setting initial values to combo box


class CourseWidgets:
    def __init__(self, frm):  # initializing frame and class
        self.frm = frm

        def callback(P):  # To validate some entry box to an integer input
            if str.isdigit(P) or P == "":
                return True
            else:
                return False

        v_cmd = (self.frm.register(callback))  # Validating input

        # WIDGETS
        # Widget - Labels
        # Defining
        self.lbl_course_name = ttk.Label(self.frm, text="Course Name",
                                         font=('Helvetica', 11))
        self.lbl_course_desc = ttk.Label(self.frm, text="Course Description",
                                         font=('Helvetica', 11))
        self.lbl_course_dur = ttk.Label(self.frm, text="Course Duration",
                                        font=('Helvetica', 11))

        # Widget - Entry box
        # Defining
        self.ent_course_name = ttk.Entry(self.frm, width=30)

        # Widget - Text box
        # Defining
        self.txt_course_desc = Text(self.frm, font=('Helvetica', 10),
                                    height=5, width=45)

        # Widget - Combo box
        # Defining
        self.combo_course_dur_y = ttk.Combobox(self.frm, state='readonly',
                                               values=["Years", 0, 1, 2, 3, 4, 5])
        self.combo_course_dur_m = ttk.Combobox(self.frm, state='readonly',
                                               values=["Months", 0, 1, 2, 3, 4, 5,
                                                       6, 7, 8, 9, 10, 11, 12])

        self.tpl_combo_box = (self.combo_course_dur_y, self.combo_course_dur_m)
        self.tpl_entry_box = (self.ent_course_name, self.txt_course_desc)
        self.set_default()

    def set_default(self):
        self.ent_course_name.delete(0, END)
        self.txt_course_desc.delete('1.0', END)
        for i in self.tpl_combo_box:
            i.current(0)
