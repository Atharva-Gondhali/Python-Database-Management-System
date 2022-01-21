# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports
from Widgets import CourseWidgets
from Course.Course_back import add_course_database


class CreateCourse:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):  # Back Function to go back a menu
            for widget in self.frm.winfo_children():
                widget.destroy()
            cls.frm.destroy()

        def clear(cls):
            cls.set_default()

        def add_course(cls):
            if (cls.combo_course_dur_y.get().isalnum() and
                    cls.combo_course_dur_m.get().isalnum()):
                duration = ((int(cls.combo_course_dur_y.get()) * 100) +
                            int(cls.combo_course_dur_m.get()))
            else:
                duration = 0

            values = (cls.ent_course_name.get(),
                      cls.txt_course_desc.get(1.0, END),
                      duration,
                      '', '', '')
            print(values)

            add_course_database(values)
            cls.set_default()

        def widgets(cls):  # Placing widgets
            # Placing label widgets
            cls.lbl_course_name.grid(row=1, column=0, padx=(40, 5),
                                     sticky=W, pady=20)
            cls.lbl_course_desc.grid(row=2, column=0, padx=(40, 5),
                                     sticky=NW, pady=20)
            cls.lbl_course_dur.grid(row=5, column=0, padx=(40, 5),
                                    sticky=W, pady=20)

            # Placing entry box widgets
            cls.ent_course_name.grid(row=1, column=1, sticky=W)

            # Placing entry box widgets
            cls.txt_course_desc.grid(row=2, column=1, pady=15)

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
                                       width=13, command=lambda: add_course(wdg))
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self), width=13)
        btn_clr_field = ttk.Button(self.frm, text="Clear fields",
                                   width=13, command=lambda: clear(wdg))

        # Placing
        btn_create_course.grid(row=13, column=1, pady=15, padx=5,
                               ipadx=6)
        btn_back.grid(row=13, column=2, pady=15, padx=4,
                      ipadx=6)
        btn_clr_field.grid(row=13, column=1, pady=15, padx=5,
                           ipadx=6, sticky=E)
