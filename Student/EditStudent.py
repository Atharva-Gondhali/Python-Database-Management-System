# IMPORTS
from tkinter import *
from tkinter import ttk     # Tkinter imports
from Student.Widgets import Widgets     # Widgets imports
from Student.Student_back import get_std_databse, update_std_database
# Backend functions imports


class EditStudent:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)      # initaializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(self):     # Back Function to go back a menu
            self.frm.destroy()

        def change_state(self, state):  # To change state of widgets
            for i in self.tpl_all_entries:
                i.configure(state=state)

        def callback(P):  # To validate some entry box to an integer input
            if str.isdigit(P) or P == "":
                return True
            else:
                return False

        def clear_fields(self):     # To clear all fields
            for i in self.tpl_entry_box:
                i.delete(0, END)

            for i in self.tpl_combo_box:
                i.current(0)

        def update_std(self):   # To update student in database
            # Function from backend file
            update_std_database(self.ent_first_name, self.ent_last_name,
                                self.ent_father_name, self.ent_email_id,
                                self.ent_age, self.combo_age_group,
                                self.combo_gender, self.combo_course,
                                self.ent_medical_com, self.ent_address,
                                self.ent_phone_number, ent_std_id)

            # Reseting widgets
            clear_fields(wdg)
            ent_std_id.delete(0, END)
            change_state(self, 'disabled')

        def get_std(self):  # To get student from database of given
            change_state(self, 'normal')  # student id and inserting
            # them in widgets
            # Function from backend file to get student
            std = get_std_databse(ent_std_id.get())

            try:    # Try and loop to insert details of student
                pos = 1
                for field in self.tpl_all_entries:
                    field.delete(0, END)
                    field.insert(0, str(std[0][pos]))
                    pos += 1

            except IndexError:  # Check if entered id is invalid
                clear_fields(wdg)
                change_state(self, 'disabled')

        def widgets(self):  # Placing widgets
            # Placing label widgets
            self.lbl_first_name.grid(row=3, column=0, padx=(40, 5),
                                     pady=5, sticky=W)
            self.lbl_last_name.grid(row=4, column=0, padx=(40, 5),
                                    pady=5, sticky=W)
            self.lbl_father_name.grid(row=5, column=0, padx=(40, 5),
                                      pady=5, sticky=W)
            self.lbl_email_id.grid(row=6, column=0, padx=(40, 5),
                                   pady=5, sticky=W)
            self.lbl_age.grid(row=7, column=0, padx=(40, 5),
                              pady=5, sticky=W)
            self.lbl_age_group.grid(row=8, column=0, padx=(40, 5),
                                    pady=5, sticky=W)
            self.lbl_gender.grid(row=9, column=0, padx=(40, 5),
                                 pady=5, sticky=W)
            self.lbl_course.grid(row=10, column=0, padx=(40, 5),
                                 pady=5, sticky=W)
            self.lbl_medical_com.grid(row=11, column=0, padx=(40, 5),
                                      pady=5, sticky=W)
            self.lbl_address.grid(row=12, column=0, padx=(40, 5),
                                  pady=5, sticky=W)
            self.lbl_phone_number.grid(row=13, column=0, padx=(40, 5),
                                       pady=5, sticky=W)

            # Placing entry box widgets
            self.ent_first_name.grid(row=3, column=1, padx=15,
                                     pady=5, sticky=EW)
            self.ent_last_name.grid(row=4, column=1, padx=15,
                                    pady=5, sticky=EW)
            self.ent_father_name.grid(row=5, column=1, padx=15,
                                      pady=5, sticky=EW)
            self.ent_email_id.grid(row=6, column=1, padx=15,
                                   pady=5, sticky=EW)
            self.ent_age.grid(row=7, column=1, padx=15,
                              pady=5, sticky=EW)
            self.ent_medical_com.grid(row=11, column=1, padx=15,
                                      pady=5, sticky=EW)
            self.ent_address.grid(row=12, column=1, padx=15,
                                  pady=5, sticky=EW)
            self.ent_phone_number.grid(row=13, column=1, padx=15,
                                       pady=5, sticky=EW)

            # Placing combo box widgets
            self.combo_age_group.grid(row=8, column=1, padx=15,
                                      pady=8, ipady=1, sticky=EW)
            self.combo_gender.grid(row=9, column=1, padx=15,
                                   pady=8, ipady=1, sticky=EW)
            self.combo_course.grid(row=10, column=1, padx=15,
                                   pady=8, ipady=1, sticky=EW)

        # WIDGETS
        wdg = Widgets(self.frm)     # Initaializing widget class
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
        vcmd = (self.frm.register(callback))  # Validation for
        # integer input
        # Defining
        ent_std_id = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(vcmd, '%P'))
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
