# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports
from Widgets import CourseWidgets
from Course.Course_back import get_update_course, update_course_database


class EditCourse:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)

        def back(cls):  # Back Function to go back a menu
            for widget in self.frm.winfo_children():
                widget.destroy()
            cls.frm.destroy()

        def clear(cls):
            cls.set_default()

        def callback(p):  # To validate some entry box to an integer input
            if str.isdigit(p) or p == "":
                return True
            else:
                return False

        def change_state(cls, state):
            cls.ent_course_name.configure(state=state)
            cls.txt_course_desc.configure(state=state)
            cls.combo_course_dur_y.configure(state=state)
            cls.combo_course_dur_m.configure(state=state)
            btn_edit_course.configure(state=state)

        def get_course(cls):
            c_id = ent_course_id.get()
            course = get_update_course(c_id)
            try:
                change_state(cls, 'normal')
                cls.txt_course_desc.insert(END, course[0][2])
                cls.ent_course_name.insert(END, course[0][1])
                cls.combo_course_dur_y.set(int(course[0][3]) % 100)
                cls.combo_course_dur_m.set(int(course[0][3]) // 100)
            except IndexError:
                clear(cls)
                change_state(cls, 'disabled')

        def update_course(cls):
            duration = ((int(cls.combo_course_dur_y.get()) * 100) +
                        int(cls.combo_course_dur_m.get()))
            values = (cls.ent_course_name.get(),
                      cls.txt_course_desc.get(1.0, END),
                      duration, ent_course_id.get())
            update_course_database(values)
            clear(cls)
            change_state(cls, 'disabled')

        def widgets(cls):  # Placing widgets
            # Placing label widgets
            cls.lbl_course_name.grid(row=4, column=0, padx=(40, 5),
                                     sticky=W, pady=20)
            cls.lbl_course_desc.grid(row=5, column=0, padx=(40, 5),
                                     sticky=NW, pady=20)
            cls.lbl_course_dur.grid(row=6, column=0, padx=(40, 5),
                                    sticky=W, pady=20)

            # Placing entry box widgets
            cls.ent_course_name.grid(row=4, column=1, sticky=W)

            # Placing entry box widgets
            cls.txt_course_desc.grid(row=5, column=1, pady=15)

            # Placing combo box widgets
            cls.combo_course_dur_y.grid(row=6, column=1, sticky=W)
            cls.combo_course_dur_m.grid(row=6, column=1, sticky=E)

        # WIDGETS
        wdg = CourseWidgets(self.frm)  # Initializing widget class
        widgets(wdg)

        # Widgets - Labels
        # Defining
        lbl_edit_std = ttk.Label(self.frm, text="Edit Course",
                                 font=('Helvetica', 16))
        lbl_course_id = ttk.Label(self.frm, text="Course ID No.",
                                  font=('Helvetica', 11))
        lbl_sel_course = ttk.Label(self.frm, text="Select Course",
                                   font=('Helvetica', 14))
        lbl_edit_std1 = ttk.Label(self.frm, text="Edit Course",
                                  font=('Helvetica', 14))

        # Placing
        lbl_edit_std.grid(row=0, column=0, padx=30, pady=15,
                          sticky=W)
        lbl_sel_course.grid(row=1, column=0, padx=30, pady=(15, 10),
                            sticky=W)
        lbl_course_id.grid(row=2, column=0, padx=30, pady=(0, 20),
                           sticky=W)
        lbl_edit_std1.grid(row=3, column=0, padx=30, pady=(10, 0),
                           sticky=W)

        # Widgets - Entry box
        v_cmd = (self.frm.register(callback))  # Validation for
        # integer input
        # Defining
        ent_course_id = ttk.Entry(self.frm, width=30, validate='all',
                                  validatecommand=(v_cmd, '%P'))
        # Placing
        ent_course_id.grid(row=2, column=1, sticky=W)

        # Widgets - Buttons
        # Defining
        btn_select = ttk.Button(self.frm, text="Select", width=15,
                                command=lambda: get_course(wdg))
        btn_edit_course = ttk.Button(self.frm, text="Update",
                                     width=13,
                                     command=lambda: update_course(wdg))
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self), width=13)

        # Placing
        btn_select.grid(row=2, column=1, sticky=E)
        btn_edit_course.grid(row=7, column=1, pady=15, padx=5,
                             ipadx=6, sticky=E)
        btn_back.grid(row=7, column=2, pady=15, padx=4,
                      ipadx=6)

        change_state(wdg, 'disabled')
