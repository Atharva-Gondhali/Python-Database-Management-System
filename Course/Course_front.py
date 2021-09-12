# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkiner Imports


class Course:
    def __init__(self, frm):
        self.frm = frm      # initaializing frame and class


    # Widgets - Labels
        # Defining
        lbl_course = ttk.Label(self.frm, text="Manage Courses",
                                font=('Helvetica', 15))

        # Placing
        lbl_course.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)

    # Widgets - Buttons
        # Defining
        btn_add_std = ttk.Button(self.frm, text="Create New Cousre",
                                 width=20)
        btn_edit_std = ttk.Button(self.frm, text="Edit Course",
                                  width=20)
        btn_view_std = ttk.Button(self.frm, text=".....",
                                  width=20)

        # Placing
        btn_add_std.grid(row=4, column=0, padx=10, pady=15,
                         ipady=8)
        btn_edit_std.grid(row=5, column=0, padx=10, pady=15,
                          ipady=8)
        btn_view_std.grid(row=6, column=0, padx=10, pady=15,
                          ipady=8)