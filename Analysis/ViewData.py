# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports
from Analysis.Analysis_back import get_std, key
from Course.Course_back import get_course_names


class ViewData:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)

    # FUNCTIONS
        def back(cls):  # Back Function to go back a menu
            for widgets in self.frm.winfo_children():
                widgets.destroy()
            cls.frm.destroy()

        def insert_records(condition='', value=''):  # Function to
            for i in tree_std.get_children():  # insert filtered values
                tree_std.delete(i)

            result = get_std(condition, value)
            std_id = 0
            try:
                for i in result:
                    tree_std.insert(parent='', index='end', iid=str(std_id), text="",
                                    values=(i[0], i[1]+' '+i[2], i[3], i[4], i[5], i[6],
                                    i[7], i[8]))
                    std_id += 1
            except IndexError:
                pass

        def set_filter2(cond1, cond2):  # Function for the second combo box
            insert_records(key[cond1], cond2)

        def set_filter1(cond1, combo2):  # Function for the first combo box
            # Checking selected condition and loading the next combo box
            if cond1 == 'Age Group':
                value = ('U-12', 'U-14', 'U-16', 'U-18', 'U-25', 'Open')
                combo2.configure(values=value, state='readonly')
            elif cond1 == 'Course':
                courses_r = get_course_names()
                courses_s = ()
                for i in courses_r:
                    courses_s += (f"{i[1]} ({i[0]})", )
                combo2.configure(values=courses_s, state='readonly')
            else:
                combo2.configure(state='disabled')
                # Refreshing the tree
                for i in tree_std.get_children():
                    tree_std.delete(i)
                insert_records()

    # TREEVIEW
        # Initializing tree view
        tree_std = ttk.Treeview(self.frm, height=22)
        tree_std.grid(row=0, column=0, columnspan=3)
        # Treeview fields
        tree_std['columns'] = ("ID No.", "Name", "Course",
                               "Age Group", "Sprint Test",
                               "Yoyo Test", "Weight Sust Test",
                               "Stamina Test")

        # TREEVIEW - Define columns
        tree_std.column("#0", width=0, stretch=NO)
        tree_std.column("ID No.", width=40, minwidth=42,
                        anchor=CENTER)
        tree_std.column("Name", width=95, minwidth=110,
                        anchor=W)
        tree_std.column("Course", width=95, minwidth=97,
                        anchor=W)
        tree_std.column("Age Group", width=75, minwidth=85,
                        anchor=W)
        tree_std.column("Sprint Test", width=75, minwidth=80,
                        anchor=CENTER)
        tree_std.column("Yoyo Test", width=75, minwidth=80,
                        anchor=CENTER)
        tree_std.column("Weight Sust Test", width=80, minwidth=100,
                        anchor=CENTER)
        tree_std.column("Stamina Test", width=80, minwidth=85,
                        anchor=CENTER)

        # TREEVIEW - Define column headings
        tree_std.heading("ID No.", text="ID No.", anchor=CENTER)
        tree_std.heading("Name", text="Name", anchor=W)
        tree_std.heading("Course", text="Course", anchor=W)
        tree_std.heading("Age Group", text="Age Group", anchor=W)
        tree_std.heading("Sprint Test", text="Sprint Test", anchor=CENTER)
        tree_std.heading("Yoyo Test", text="Yoyo Test", anchor=CENTER)
        tree_std.heading("Weight Sust Test",
                         text="Weight Sust Test", anchor=CENTER)
        tree_std.heading("Stamina Test", text="Stamina Test", anchor=CENTER)

        # TREEVIEW - Scrollbar
        v_scrollbar = ttk.Scrollbar(self.frm, orient='vertical')
        h_scrollbar = ttk.Scrollbar(self.frm, orient='horizontal')

        v_scrollbar.configure(command=tree_std.yview)
        h_scrollbar.configure(command=tree_std.xview)

        tree_std.configure(yscrollcommand=v_scrollbar.set,
                           xscrollcommand=h_scrollbar.set)

        h_scrollbar.grid(row=1, column=0, columnspan=3, sticky=EW)
        v_scrollbar.grid(row=0, column=3, sticky=NS)

        insert_records()

        # WIDGETS
        # Widgets - Buttons
        # Defining
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self))

        # Placing
        btn_back.grid(row=2, column=2, sticky=E, pady=(11, 0))

        # Widgets - Labels
        # Defining
        lbl_filter = ttk.Label(self.frm, text="Filter",
                               font=('Helvetica', 10))

        # Placing
        lbl_filter.grid(row=2, column=0, pady=(11, 0), sticky=E)

        # Widgets - Combobox
        # Defining
        combo_filter1 = ttk.Combobox(self.frm,
                                     values=['None', 'Age Group', 'Course'],
                                     state='readonly')
        combo_filter2 = ttk.Combobox(self.frm, state='disabled')

        combo_filter1.current(0)
        # Event binding
        combo_filter1.bind("<FocusIn>", lambda event: set_filter1(
            combo_filter1.get(), combo_filter2))
        combo_filter2.bind("<FocusIn>", lambda event: set_filter2(
            combo_filter1.get(), combo_filter2.get()))

        # Placing
        combo_filter1.grid(row=2, column=1, pady=(11, 0))
        combo_filter2.grid(row=2, column=2, pady=(11, 0), sticky=W)
