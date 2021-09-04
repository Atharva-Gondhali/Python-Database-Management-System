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