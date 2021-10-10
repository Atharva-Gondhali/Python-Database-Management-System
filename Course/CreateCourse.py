# IMPORTS
from tkinter import *
from tkinter import ttk     # Tkinter imports


class CreateCourse:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)      # initaializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(self):     # Back Function to go back a menu
            self.frm.destroy()

        # Widgets - Labels
        # Defining
        lbl_add_std = ttk.Label(self.frm, text="Create Course",
                                font=('Helvetica', 15))

        # Placing
        lbl_add_std.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)
                
        # Widgets - Buttons
        # Defining
        btn_add_std = ttk.Button(self.frm, text="Add Student")
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self))
        btn_clr_field = ttk.Button(self.frm, text="Clear fields")

        # Placing
        btn_add_std.grid(row=12, column=2, pady=8, padx=10,
                         ipadx=6)
        btn_back.grid(row=12, column=3, pady=8, padx=10,
                      ipadx=6)
        btn_clr_field.grid(row=12, column=1, pady=8, padx=10,
                           ipadx=6, sticky=E)