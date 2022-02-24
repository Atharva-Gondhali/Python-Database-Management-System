# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter Imports
from Analysis.AddData import AddData
from Analysis.ViewData import ViewData


class Analysis:
    def __init__(self, frm):
        self.frm = frm  # initializing frame and class

        # FUNCTIONS
        def add_data(cls):  # To open Add Student Menu
            frame_add_std = ttk.Frame(cls.frm, width=635, height=535)

            AddData(frame_add_std)

        def view_data(cls):  # To open Edit Student Menu
            frame_edit_std = ttk.Frame(cls.frm, width=635, height=535)

            ViewData(frame_edit_std)

        # Widgets - Labels
        # Defining
        lbl_student = ttk.Label(self.frm, text="Physical Analysis",
                                font=('Helvetica', 15))

        # Placing
        lbl_student.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)

        # Widgets - Buttons
        # Defining
        btn_add_ana = ttk.Button(self.frm, text="Add/Update Data",
                                 width=20, command=lambda: add_data(self))
        btn_view_ana = ttk.Button(self.frm, text="View Students",
                                  width=20, command=lambda: view_data(self))

        # Placing
        btn_add_ana.grid(row=1, column=0, padx=10, pady=15,
                         ipady=8)
        btn_view_ana.grid(row=2, column=0, padx=10, pady=15,
                          ipady=8)
