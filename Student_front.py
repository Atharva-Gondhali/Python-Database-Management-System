from tkinter import ttk

from Student.AddStudent import *
from Student.EditStudent import *
from Student.ViewStudent import *


class Student:
    def __init__(self, frm):
        self.frm = frm

        def add_std(self):
            frame_add_std = ttk.Frame(self.frm, width=635, height=535)

            std = AddStudent(frame_add_std)

        def edit_std(self):
            frame_edit_std = ttk.Frame(self.frm, width=635, height=535)

            std = EditStudent(frame_edit_std)

        def view_std(self):
            frame_view_std = ttk.Frame(self.frm, width=635, height=535)

            std = ViewStudent(frame_view_std)

        def update(self, event, condition):
            values = []
            tpl = get_data(self, condition)
            print(tpl)
            for i in tpl:
                for j in i:
                    if combo_main.get() in str(j) and combo_main.get() != '':
                        values.append(j) 
    
            combo_main.configure(values = values)

        def get_data(self, condition):
            if condition == 'First name':
                return get_all_std_database('first_name', '')
            elif condition == 'Last name':
                return get_all_std_database('last_name', '')
            elif condition == 'Father\'s name':
                return get_all_std_database('father_name', '')
            elif condition == 'Email id':
                return get_all_std_database('email_id', '')
            elif condition == 'Phone number':
                return get_all_std_database('phone_no', '')
            else:
                return get_all_std_database('first_name', '')

        # Label students
        lbl_student = ttk.Label(self.frm, text="Manage Students",
                                font=('Helvetica', 15))
        lbl_search = ttk.Label(self.frm, text = "Search student",
                                font = ('Helvetica', 13))
        lbl_functions = ttk.Label(self.frm, text = "Functions",
                                font = ('Helvetica', 13))

        lbl_student.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)
        lbl_search.grid(row = 1, column = 0, padx=(30, 10), pady=15,
                        sticky = EW)
        lbl_functions.grid(row = 3, column = 0, padx=(30, 10), pady=15,
                        sticky = EW)

        # Buttons Students
        btn_add_std = ttk.Button(self.frm, text="Admit Student",
                                 width=20, command=lambda: add_std(self))
        btn_edit_std = ttk.Button(self.frm, text="Edit Student",
                                  width=20, command=lambda: edit_std(self))
        btn_view_std = ttk.Button(self.frm, text="View Students",
                                  width=20, command=lambda: view_std(self))

        btn_add_std.grid(row=4, column=0, padx=10, pady=15,
                         ipady=8)
        btn_edit_std.grid(row=5, column=0, padx=10, pady=15,
                          ipady=8)
        btn_view_std.grid(row=6, column=0, padx=10, pady=15,
                          ipady=8)

        
        # COMBO BOX
        filters = ['Search by...', 'First name', 'Last name', 'Father\'s name',
                    'Email id', 'Phone number']
        combo_main = ttk.Combobox(self.frm, width = 24, 
                                  font = ('Helvetica', 12))
        combo_select = ttk.Combobox(self.frm, width = 15, 
                                    font = ('Helvetica', 12), 
                                    values = filters)
        
        combo_select.current(0)
        combo_main.bind("<KeyRelease>", lambda event: 
                        update(self, event, combo_select.get()))

        combo_main.grid(row = 2, column = 0, padx = (30, 5),
                        pady = (5, 20))
        combo_select.grid(row = 2, column = 1, padx = (10, 5),
                        pady = (14, 30), sticky = W)
