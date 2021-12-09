# IMPORTS
from tkinter import *
from tkinter import ttk     # Tkinter imports
from Widgets import StudentWidgets     # Widget imports


class SearchStudent:
    def __init__(self, frm, tpl):
        self.tpl = tpl
        self.frm = frm
        self.frm.grid_propagate(0)          # initializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):     # Back Function to go back a menu
            cls.frm.destroy()

        def widgets(cls):  # Placing widgets
            # Placing label widgets
            cls.lbl_father_name.grid(row=1, column=1, padx=(40, 5),
                                     pady=(20, 5), sticky=W)
            cls.lbl_email_id.grid(row=3, column=0, padx=(30, 40), pady=(15, 5),
                                  sticky=W)
            cls.lbl_age.grid(row=3, column=1, padx=(40, 5),
                             pady=(15, 5), sticky=W)
            cls.lbl_age_group.grid(row=5, column=0, padx=(30, 40), pady=(15, 5),
                                   sticky=W)
            cls.lbl_gender.grid(row=5, column=1, padx=(40, 5),
                                pady=(15, 5), sticky=W)
            cls.lbl_course.grid(row=7, column=0, padx=(30, 40), pady=(15, 5),
                                sticky=W)
            cls.lbl_medical_com.grid(row=7, column=1, padx=(40, 5),
                                     pady=(15, 5), sticky=W)
            cls.lbl_address.grid(row=9, column=0, padx=(30, 40), pady=(15, 5),
                                 sticky=W)
            cls.lbl_phone_number.grid(row=9, column=1, padx=(40, 5),
                                      pady=(15, 0), sticky=W)

        # WIDGETS
        wdg = StudentWidgets(self.frm)     # Initializing widget class
        widgets(wdg)

        # Widgets - Labels
        # Defining
        lbl_heading = ttk.Label(self.frm, text="Search Student",
                                font=('Helvetica', 14))
        lbl_student = ttk.Label(self.frm, text="Student",
                                font=('Helvetica', 11))
        lbl_student_val = ttk.Label(self.frm,
                                    text=self.tpl[1]+' '+self.tpl[2],
                                    font=('Helvetica', 13))
        lbl_father = ttk.Label(self.frm, text=self.tpl[3],
                               font=('Helvetica', 13))
        lbl_email = ttk.Label(self.frm, text=self.tpl[4],
                              font=('Helvetica', 13))
        lbl_age = ttk.Label(self.frm, text=self.tpl[5],
                            font=('Helvetica', 13))
        lbl_age_group = ttk.Label(self.frm, text=self.tpl[6],
                                  font=('Helvetica', 13))
        lbl_gender = ttk.Label(self.frm, text=self.tpl[7],
                               font=('Helvetica', 13))
        lbl_course = ttk.Label(self.frm, text=self.tpl[8],
                               font=('Helvetica', 13))
        lbl_medical = ttk.Label(self.frm, text=self.tpl[9],
                                font=('Helvetica', 13))
        lbl_address = ttk.Label(self.frm, text=self.tpl[10],
                                font=('Helvetica', 13))
        lbl_phone = ttk.Label(self.frm, text=self.tpl[11],
                              font=('Helvetica', 13))

        # Placing
        lbl_heading.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W, columnspan=2)
        lbl_student.grid(row=1, column=0, padx=30, pady=(20, 5),
                         sticky=W)
        lbl_student_val.grid(row=2, column=0, padx=(30, 5),
                             pady=3, sticky=W)
        lbl_father.grid(row=2, column=1, padx=(40, 5),
                        pady=3, sticky=W)
        lbl_email.grid(row=4, column=0, padx=(30, 40), pady=(3, 15),
                       sticky=W)
        lbl_age.grid(row=4, column=1, padx=(40, 5),
                     pady=3, sticky=NW)
        lbl_age_group.grid(row=6, column=0, padx=(30, 40), pady=(3, 15),
                           sticky=W)
        lbl_gender.grid(row=6, column=1, padx=(40, 5),
                        pady=3, sticky=NW)
        lbl_course.grid(row=8, column=0, padx=(30, 40), pady=(3, 15),
                        sticky=W)
        lbl_medical.grid(row=8, column=1, padx=(40, 5),
                         pady=3, sticky=W)
        lbl_address.grid(row=10, column=0, padx=(30, 40), pady=(3, 15),
                         sticky=W)
        lbl_phone.grid(row=10, column=1, padx=(40, 5),
                       pady=3, sticky=NW)

        # Widgets - Buttons
        # Defining
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self))

        # Placing
        btn_back.grid(row=11, column=2, padx=10, pady=10,
                      sticky=E, ipadx=6)
