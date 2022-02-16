# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports


class AddData:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)

        # Widgets - Labels
        # Defining
        lbl_add_std = ttk.Label(self.frm, text="Add-Update Data",
                                font=('Helvetica', 15))

        # Placing
        lbl_add_std.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)