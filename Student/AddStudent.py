# IMPORTS
from tkinter import *
from tkinter import ttk     # Tkinter imports
from Widgets import StudentWidgets     # Widget imports
from Student.Student_back import add_std_database
# Backend functions imports


class AddStudent:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)      # initializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):     # Back Function to go back a menu
            cls.frm.destroy()

        def clear_fields(cls):     # To clear all fields
            for i in cls.tpl_entry_box:
                i.delete(0, END)

            for i in cls.tpl_combo_box:
                i.current(0)

        def add_std(cls):      # To add student to database
            # Function from backend b_file
            add_std_database(cls.ent_first_name, cls.ent_last_name,
                             cls.ent_father_name, cls.ent_email_id,
                             cls.ent_age, cls.combo_age_group,
                             cls.combo_gender, cls.combo_course,
                             cls.ent_medical_com, cls.ent_address,
                             cls.ent_phone_number)
            clear_fields(cls)

        def widgets(cls):  # Placing widgets
            # Placing label widgets
            cls.lbl_first_name.grid(row=1, column=0, padx=(40, 5),
                                    pady=8, sticky=W)
            cls.lbl_last_name.grid(row=2, column=0, padx=(40, 5),
                                   pady=8, sticky=W)
            cls.lbl_father_name.grid(row=3, column=0, padx=(40, 5),
                                     pady=8, sticky=W)
            cls.lbl_email_id.grid(row=4, column=0, padx=(40, 5),
                                  pady=8, sticky=W)
            cls.lbl_age.grid(row=5, column=0, padx=(40, 5),
                             pady=8, sticky=W)
            cls.lbl_age_group.grid(row=6, column=0, padx=(40, 5),
                                   pady=8, sticky=W)
            cls.lbl_gender.grid(row=7, column=0, padx=(40, 5),
                                pady=8, sticky=W)
            cls.lbl_course.grid(row=8, column=0, padx=(40, 5),
                                pady=8, sticky=W)
            cls.lbl_medical_com.grid(row=9, column=0, padx=(40, 5),
                                     pady=8, sticky=W)
            cls.lbl_address.grid(row=10, column=0, padx=(40, 5),
                                 pady=8, sticky=W)
            cls.lbl_phone_number.grid(row=11, column=0, padx=(40, 5),
                                      pady=8, sticky=W)

            # Placing entry box widgets
            cls.ent_first_name.grid(row=1, column=1, padx=15,
                                    pady=8, sticky=E, ipady=1)
            cls.ent_last_name.grid(row=2, column=1, padx=15,
                                   pady=8, sticky=EW, ipady=1)
            cls.ent_father_name.grid(row=3, column=1, padx=15,
                                     pady=8, sticky=EW, ipady=1)
            cls.ent_email_id.grid(row=4, column=1, padx=15,
                                  pady=8, sticky=EW, ipady=1)
            cls.ent_age.grid(row=5, column=1, padx=15,
                             pady=8, sticky=EW, ipady=1)
            cls.ent_medical_com.grid(row=9, column=1, padx=15,
                                     pady=8, sticky=EW, ipady=1)
            cls.ent_address.grid(row=10, column=1, padx=15,
                                 pady=8, sticky=EW, ipady=1)
            cls.ent_phone_number.grid(row=11, column=1, padx=15,
                                      pady=8, sticky=EW, ipady=1)

            # Placing combo box widgets
            cls.combo_age_group.grid(row=6, column=1, padx=15,
                                     pady=8, ipady=1, sticky=EW)
            cls.combo_gender.grid(row=7, column=1, padx=15,
                                  pady=8, ipady=1, sticky=EW)
            cls.combo_course.grid(row=8, column=1, padx=15,
                                  pady=8, ipady=1, sticky=EW)

        # WIDGETS
        wdg = StudentWidgets(self.frm)     # Initializing widget class
        widgets(wdg)

        # Widgets - Labels
        # Defining
        lbl_add_std = ttk.Label(self.frm, text="Admit Student",
                                font=('Helvetica', 15))

        # Placing
        lbl_add_std.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)

        # Widgets - Buttons
        # Defining
        btn_add_std = ttk.Button(self.frm, text="Add Student",
                                 command=lambda: add_std(wdg))
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self))
        btn_clr_field = ttk.Button(self.frm, text="Clear fields",
                                   command=lambda: clear_fields(wdg))

        # Placing
        btn_add_std.grid(row=12, column=2, pady=8, padx=10,
                         ipadx=6)
        btn_back.grid(row=12, column=3, pady=8, padx=10,
                      ipadx=6)
        btn_clr_field.grid(row=12, column=1, pady=8, padx=10,
                           ipadx=6, sticky=E)
