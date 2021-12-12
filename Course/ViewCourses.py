from tkinter import *
from tkinter import ttk  # Tkinter Imports
from Course.Course_back import get_all_courses


class ViewCourse:
    def __init__(self, frm):  # initializing frame and class
        self.frm = frm
        self.frm.grid_propagate(0)
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):  # Back Function to go back a menu
            for widget in self.frm.winfo_children():
                widget.destroy()
            cls.frm.destroy()

        def insert_records():
            result = get_all_courses()
            crs_id = 0
            for i in result:
                tree_std.insert(parent='', index='end', iid=str(crs_id), text="",
                                values=(i[0], i[1], i[2], f"{i[3]//100}, {i[3]%100}",
                                        i[4], i[5], i[6]))
                crs_id += 1

        # TREEVIEW
        # Initializing tree view
        tree_std = ttk.Treeview(self.frm, height=22)
        tree_std.grid(row=0, column=0, columnspan=3)
        # Treeview fields
        tree_std['columns'] = ("ID No.", "Name", "Description",
                               "Duration", "Test1",
                               "Test2", "Test3")

        # TREEVIEW - Define columns
        tree_std.column("#0", width=0, stretch=NO)
        tree_std.column("ID No.", width=50, minwidth=55,
                        anchor=CENTER)
        tree_std.column("Name", width=95, minwidth=100,
                        anchor=W)
        tree_std.column("Description", width=125, minwidth=130,
                        anchor=W)
        tree_std.column("Duration", width=99, minwidth=100,
                        anchor=CENTER)
        tree_std.column("Test1", width=80, minwidth=90,
                        anchor=CENTER)
        tree_std.column("Test2", width=80, minwidth=90,
                        anchor=CENTER)
        tree_std.column("Test3", width=80, minwidth=90,
                        anchor=CENTER)

        # TREEVIEW - Define column headings
        tree_std.heading("ID No.", text="ID No.", anchor=CENTER)
        tree_std.heading("Name", text="Name", anchor=W)
        tree_std.heading("Description", text="Description", anchor=W)
        tree_std.heading("Duration", text="Duration(Y,M)", anchor=CENTER)
        tree_std.heading("Test1", text="Test 1", anchor=CENTER)
        tree_std.heading("Test2", text="Test 2", anchor=CENTER)
        tree_std.heading("Test3", text="Test 3", anchor=CENTER)

        # TREEVIEW - Adding records
        insert_records()

        # TREEVIEW - Scrollbar
        v_scrollbar = ttk.Scrollbar(self.frm, orient='vertical')
        h_scrollbar = ttk.Scrollbar(self.frm, orient='horizontal')

        v_scrollbar.configure(command=tree_std.yview)
        h_scrollbar.configure(command=tree_std.xview)

        tree_std.configure(yscrollcommand=v_scrollbar.set,
                           xscrollcommand=h_scrollbar.set)

        h_scrollbar.grid(row=1, column=0, columnspan=3, sticky=EW)
        v_scrollbar.grid(row=0, column=3, sticky=NS)

        # WIDGETS
        # Widgets - Buttons
        # Defining
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self))

        # Placing
        btn_back.grid(row=2, column=2, sticky=E, pady=(11, 0))
