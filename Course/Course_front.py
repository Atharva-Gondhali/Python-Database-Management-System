# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter Imports
from Course.CreateCourse import CreateCourse  # All Course function
from Course.EditCourse import EditCourse
from Course.ViewCourses import ViewCourse
from Course.CourseTest import CourseTest


class Course:
    def __init__(self, frm):
        self.frm = frm  # initializing frame and class

        # FUNCTIONS
        def create_course(cls):  # To open create Course Menu
            frame_create_course = ttk.Frame(cls.frm, width=635, height=535)

            CreateCourse(frame_create_course)

        def edit_course(cls):
            frame_edit_course = ttk.Frame(cls.frm, width=635, height=535)

            EditCourse(frame_edit_course)

        def view_course(cls):
            frame_view_course = ttk.Frame(cls.frm, width=635, height=535)

            ViewCourse(frame_view_course)

        def course_test(cls):
            frame_course_test = ttk.Frame(cls.frm, width=635, height=535)

            CourseTest(frame_course_test)


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
                                     width=20, command=lambda: edit_course(self))
        btn_view_course = ttk.Button(self.frm, text="View Courses",
                                     width=20, command=lambda: view_course(self))
        btn_add_test = ttk.Button(self.frm, text="Add Test",
                                     width=20, command=lambda: course_test(self))

        # Placing
        btn_create_course.grid(row=4, column=0, padx=10, pady=15,
                               ipady=8)
        btn_edit_course.grid(row=5, column=0, padx=10, pady=15,
                             ipady=8)
        btn_view_course.grid(row=6, column=0, padx=10, pady=15,
                             ipady=8)
        btn_add_test.grid(row=7, column=0, padx=10, pady=15,
                             ipady=8)
