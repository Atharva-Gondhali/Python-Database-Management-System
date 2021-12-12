# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter Imports
from Student.AddStudent import AddStudent  # All student function
from Student.EditStudent import EditStudent  # classes imports
from Student.ViewStudent import ViewStudent
from Student.SearchStudent import SearchStudent
from Student.Student_back import get_all_std_database, key


# Backend functions imports


class Student:
    def __init__(self, frm):
        self.frm = frm  # initializing frame and class

        # FUNCTIONS
        def add_std(cls):  # To open Add Student Menu
            frame_add_std = ttk.Frame(cls.frm, width=635, height=535)

            AddStudent(frame_add_std)

        def edit_std(cls):  # To open Edit Student Menu
            frame_edit_std = ttk.Frame(cls.frm, width=635, height=535)

            EditStudent(frame_edit_std)

        def view_std(cls):  # To open View Student Menu
            frame_view_std = ttk.Frame(cls.frm, width=635, height=535)

            ViewStudent(frame_view_std)

        def update_record(condition):  # To fetch search results
            values = []
            tpl = get_all_std_database(key[condition])
            for i in tpl:
                if combo_main.get() in str(i[1]) and combo_main.get() != '':
                    values.append(str(i[0]) + '. ' + str(i[1]))

            combo_main.configure(values=values)

        def show_std(value):  # To open student view menu
            std_id = value[0]
            tpl = get_all_std_database('student_id', std_id)

            frame_sea_std = ttk.Frame(self.frm, width=635, height=535)
            SearchStudent(frame_sea_std, tpl[0])

        # Widgets - Labels
        # Defining
        lbl_student = ttk.Label(self.frm, text="Manage Students",
                                font=('Helvetica', 15))
        lbl_search = ttk.Label(self.frm, text="Search student",
                               font=('Helvetica', 13))
        lbl_functions = ttk.Label(self.frm, text="Functions",
                                  font=('Helvetica', 13))

        # Placing
        lbl_student.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)
        lbl_search.grid(row=1, column=0, padx=(30, 10), pady=15,
                        sticky=EW)
        lbl_functions.grid(row=3, column=0, padx=(30, 10), pady=15,
                           sticky=EW)

        # Widgets - Buttons
        # Defining
        btn_add_std = ttk.Button(self.frm, text="Admit Student",
                                 width=20, command=lambda: add_std(self))
        btn_edit_std = ttk.Button(self.frm, text="Edit Student",
                                  width=20, command=lambda: edit_std(self))
        btn_view_std = ttk.Button(self.frm, text="View Students",
                                  width=20, command=lambda: view_std(self))
        btn_search_std = ttk.Button(self.frm, text="Select",
                                    command=lambda: show_std(combo_main.get()))

        # Placing
        btn_add_std.grid(row=4, column=0, padx=10, pady=15,
                         ipady=8)
        btn_edit_std.grid(row=5, column=0, padx=10, pady=15,
                          ipady=8)
        btn_view_std.grid(row=6, column=0, padx=10, pady=15,
                          ipady=8)
        btn_search_std.grid(row=2, column=2, padx=10)

        # Widgets - Buttons
        # Defining
        filters = ['Search by...', 'First name', 'Last name', 'Father\'s name',
                   'Email id', 'Phone number']
        combo_main = ttk.Combobox(self.frm, width=26,
                                  font=('Helvetica', 10))
        combo_select = ttk.Combobox(self.frm, width=15,
                                    font=('Helvetica', 10),
                                    values=filters, state='readonly')

        combo_select.current(0)
        combo_main.bind("<KeyRelease>", lambda event: update_record(combo_select.get()))

        # Placing
        combo_main.grid(row=2, column=0, padx=(30, 5),
                        pady=(20, 20))
        combo_select.grid(row=2, column=1, padx=(10, 5),
                          pady=(28, 30), sticky=W)
