# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports
from Widgets import CourseWidgets


class CreateCourse:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):  # Back Function to go back a menu
            cls.frm.destroy()

        def widgets(cls):  # Placing widgets
            # Placing label widgets
            cls.lbl_course_name.grid(row=1, column=0, padx=(40, 5),
                                     sticky=W, pady=8)
            cls.lbl_course_desc.grid(row=2, column=0, padx=(40, 5),
                                     sticky=NW, pady=8)
            cls.lbl_course_dur.grid(row=5, column=0, padx=(40, 5),
                                    sticky=W, pady=8)
            # self.lbl_test1.grid(row=6, column=0, padx=(40, 5),
            #                     sticky=W, pady=8)
            # self.test_name1.grid(row=7, column=0, padx=(55, 5),
            #                      sticky=W, pady=5)
            # self.test_period1.grid(row=8, column=0, padx=(55, 5),
            #                        sticky=W, pady=5)
            # self.lbl_test2.grid(row=9, column=0, padx=(40, 5),
            #                     sticky=W, pady=8)
            # self.test_name2.grid(row=10, column=0, padx=(55, 5),
            #                      sticky=W, pady=5)
            # self.test_period2.grid(row=11, column=0, padx=(55, 5),
            #                        sticky=W, pady=5)
            # self.lbl_test3.grid(row=12, column=0, padx=(40, 5),
            #                     sticky=W, pady=8)
            # self.test_name3.grid(row=13, column=0, padx=(55, 5),
            #                      sticky=W, pady=5)
            # self.test_period3.grid(row=14, column=0, padx=(55, 5),
            #                        sticky=W, pady=5)

            # Placing entry box widgets
            cls.ent_course_name.grid(row=1, column=1, sticky=W)
            # self.ent_test_name1.grid(row = 7, column = 1, sticky = W)
            # self.ent_test_name2.grid(row = 10, column = 1, sticky = W)
            # self.ent_test_name3.grid(row = 13, column = 1, sticky = W)
            # self.ent_test_dur1.grid(row = 8, column = 1, sticky = W)
            # self.ent_test_dur2.grid(row = 11, column = 1, sticky = W)
            # self.ent_test_dur3.grid(row = 14, column = 1, sticky = W)

            # Placing entry box widgets
            cls.txt_course_desc.grid(row=2, column=1, pady=10)

            # Placing combo box widgets
            cls.combo_course_dur_y.grid(row=5, column=1, sticky=W)
            cls.combo_course_dur_m.grid(row=5, column=1, sticky=E)

        # WIDGETS
        wdg = CourseWidgets(self.frm)  # Initializing widget class
        widgets(wdg)

        # Widgets - Labels
        # Defining
        lbl_add_std = ttk.Label(self.frm, text="Create Course",
                                font=('Helvetica', 15))

        # Placing
        lbl_add_std.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)

        # Widgets - Buttons
        # Defining
        btn_create_course = ttk.Button(self.frm, text="Create Course",
                                       width=13)
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self), width=13)
        btn_clr_field = ttk.Button(self.frm, text="Clear fields",
                                   width=13)

        # Placing
        btn_create_course.grid(row=13, column=1, pady=8, padx=5,
                               ipadx=6, sticky=E)
        btn_back.grid(row=14, column=2, pady=8, padx=5,
                      ipadx=6)
        btn_clr_field.grid(row=14, column=1, pady=8, padx=5,
                           ipadx=6, sticky=E)
