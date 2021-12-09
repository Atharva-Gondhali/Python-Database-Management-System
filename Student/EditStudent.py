# IMPORTS
from tkinter import *
from tkinter import ttk     # Tkinter imports
from Widgets import StudentWidgets     # Widget imports
from Student.Student_back import get_std_database, update_std_database
# Backend functions imports


class EditStudent:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)      # initializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):     # Back Function to go back a menu
            cls.frm.destroy()

        def change_state(cls, state):  # To change state of widgets
            for i in cls.tpl_all_entries:
                i.configure(state=state)
            if state == 'normal':
                for i in cls.tpl_combo_box:
                    i.configure(state='readonly')

        def callback(p):  # To validate some entry box to an integer input
            if str.isdigit(p) or p == "":
                return True
            else:
                return False

        def clear_fields(cls):     # To clear all fields
            for i in cls.tpl_entry_box:
                i.delete(0, END)

            for i in cls.tpl_combo_box:
                i.current(0)

        def update_std(cls):   # To update student in database
            # Function from backend b_file
            update_std_database(cls.ent_first_name, cls.ent_last_name,
                                cls.ent_father_name, cls.ent_email_id,
                                cls.ent_age, cls.combo_age_group,
                                cls.combo_gender, cls.combo_course,
                                cls.ent_medical_com, cls.ent_address,
                                cls.ent_phone_number, ent_std_id)

            # Resetting widgets
            clear_fields(wdg)
            ent_std_id.delete(0, END)
            change_state(cls, 'disabled')

        def get_std(cls):  # To get student from database of given
            change_state(cls, 'normal')  # student id and inserting
            # Then in widgets
            # Function from backend b_file to get student
            std = get_std_database(ent_std_id.get())

            try:    # Try and loop to insert details of student
                pos = 1
                for field in cls.tpl_all_entries:
                    field.delete(0, END)
                    field.insert(0, str(std[0][pos]))
                    pos += 1

            except IndexError:  # Check if entered id is invalid
                clear_fields(wdg)
                change_state(cls, 'disabled')

        def widgets(cls):  # Placing widgets
            # Placing label widgets
            cls.lbl_first_name.grid(row=3, column=0, padx=(40, 5),
                                    pady=5, sticky=W)
            cls.lbl_last_name.grid(row=4, column=0, padx=(40, 5),
                                   pady=5, sticky=W)
            cls.lbl_father_name.grid(row=5, column=0, padx=(40, 5),
                                     pady=5, sticky=W)
            cls.lbl_email_id.grid(row=6, column=0, padx=(40, 5),
                                  pady=5, sticky=W)
            cls.lbl_age.grid(row=7, column=0, padx=(40, 5),
                             pady=5, sticky=W)
            cls.lbl_age_group.grid(row=8, column=0, padx=(40, 5),
                                   pady=5, sticky=W)
            cls.lbl_gender.grid(row=9, column=0, padx=(40, 5),
                                pady=5, sticky=W)
            cls.lbl_course.grid(row=10, column=0, padx=(40, 5),
                                pady=5, sticky=W)
            cls.lbl_medical_com.grid(row=11, column=0, padx=(40, 5),
                                     pady=5, sticky=W)
            cls.lbl_address.grid(row=12, column=0, padx=(40, 5),
                                 pady=5, sticky=W)
            cls.lbl_phone_number.grid(row=13, column=0, padx=(40, 5),
                                      pady=5, sticky=W)

            # Placing entry box widgets
            cls.ent_first_name.grid(row=3, column=1, padx=15,
                                    pady=5, sticky=EW)
            cls.ent_last_name.grid(row=4, column=1, padx=15,
                                   pady=5, sticky=EW)
            cls.ent_father_name.grid(row=5, column=1, padx=15,
                                     pady=5, sticky=EW)
            cls.ent_email_id.grid(row=6, column=1, padx=15,
                                  pady=5, sticky=EW)
            cls.ent_age.grid(row=7, column=1, padx=15,
                             pady=5, sticky=EW)
            cls.ent_medical_com.grid(row=11, column=1, padx=15,
                                     pady=5, sticky=EW)
            cls.ent_address.grid(row=12, column=1, padx=15,
                                 pady=5, sticky=EW)
            cls.ent_phone_number.grid(row=13, column=1, padx=15,
                                      pady=5, sticky=EW)

            # Placing combo box widgets
            cls.combo_age_group.grid(row=8, column=1, padx=15,
                                     pady=8, ipady=1, sticky=EW)
            cls.combo_gender.grid(row=9, column=1, padx=15,
                                  pady=8, ipady=1, sticky=EW)
            cls.combo_course.grid(row=10, column=1, padx=15,
                                  pady=8, ipady=1, sticky=EW)

        # WIDGETS
        wdg = StudentWidgets(self.frm)     # Initializing widget class
        widgets(wdg)
        change_state(wdg, 'disabled')  # Init for first run

        # Widgets - Labels
        # Defining
        lbl_sel_std = ttk.Label(self.frm, text="Select Student",
                                font=('Helvetica', 14))
        lbl_std_id = ttk.Label(self.frm, text="Student's ID No.",
                               font=('Helvetica', 11))
        lbl_edit_std = ttk.Label(self.frm, text="Edit Student",
                                 font=('Helvetica', 14))

        # Placing
        lbl_sel_std.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)
        lbl_std_id.grid(row=1, column=0, padx=30,
                        sticky=W)
        lbl_edit_std.grid(row=2, column=0, padx=30, pady=15,
                          sticky=W)

        # Widgets - Entry box
        v_cmd = (self.frm.register(callback))  # Validation for
        # integer input
        # Defining
        ent_std_id = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(v_cmd, '%P'))
        # Placing
        ent_std_id.grid(row=1, column=1, padx=15)

        # Widgets - Buttons
        # Defining
        btn_select = ttk.Button(self.frm, text="Select", width=15,
                                command=lambda: get_std(wdg))
        btn_update = ttk.Button(self.frm, text="Update", width=13,
                                command=lambda: update_std(wdg))
        btn_back = ttk.Button(self.frm, text="Back", width=13,
                              command=lambda: back(self))

        # Placing
        btn_select.grid(row=1, column=2, sticky=W)
        btn_update.grid(row=14, column=2, padx=10)
        btn_back.grid(row=14, column=3, padx=10)
