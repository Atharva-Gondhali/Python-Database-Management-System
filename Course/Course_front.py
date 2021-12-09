# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter Imports
from Course.CreateCourse import CreateCourse  # All Course function


class Course:
    def __init__(self, frm):
        self.frm = frm  # initializing frame and class

        # FUNCTIONS
        def create_course(cls):  # To open create Course Menu
            frame_create_course = ttk.Frame(cls.frm, width=635, height=535)

            course = CreateCourse(frame_create_course)

        # Widgets - Labels
        # Defining
        lbl_course = ttk.Label(self.frm, text="Manage Courses",
                               font=('Helvetica', 15))

        # Placing
        lbl_course.grid(row=0, column=0, padx=30, pady=15,
                        sticky=W)

        # Widgets - Buttons
        # Defining
        btn_create_course = ttk.Button(self.frm, text="Create New Course",
                                       width=20, command=lambda: create_course(self))
        btn_edit_course = ttk.Button(self.frm, text="Edit Course",
                                     width=20)
        btn_view_course = ttk.Button(self.frm, text=".....",
                                     width=20)

        # Placing
        btn_create_course.grid(row=4, column=0, padx=10, pady=15,
                               ipady=8)
        btn_edit_course.grid(row=5, column=0, padx=10, pady=15,
                             ipady=8)
        btn_view_course.grid(row=6, column=0, padx=10, pady=15,
                             ipady=8)
