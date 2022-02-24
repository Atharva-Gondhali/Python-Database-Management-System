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
                                values=(i[0], i[1], i[2], f"{i[3]//100}, {i[3]%100}"))
                crs_id += 1

        # TREEVIEW
        # Initializing tree view
        tree_std = ttk.Treeview(self.frm, height=22)
        tree_std.grid(row=0, column=0, columnspan=3, padx = (40, 0),
                      pady = (20, 0))
        # Treeview fields
        tree_std['columns'] = ("ID No.", "Name", "Description",
                               "Duration")

        # TREEVIEW - Define columns
        tree_std.column("#0", width=0, stretch=NO)
        tree_std.column("ID No.", width=60, minwidth=60,
                        anchor=CENTER)
        tree_std.column("Name", width=110, minwidth=110,
                        anchor=W)
        tree_std.column("Description", width=200, minwidth=200,
                        anchor=W)
        tree_std.column("Duration", width=100, minwidth=100,
                        anchor=CENTER)

        # TREEVIEW - Define column headings
        tree_std.heading("ID No.", text="ID No.", anchor=CENTER)
        tree_std.heading("Name", text="Name", anchor=W)
        tree_std.heading("Description", text="Description", anchor=W)
        tree_std.heading("Duration", text="Duration(Y,M)", anchor=CENTER)

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
        v_scrollbar.grid(row=0, column=3, sticky=NS, pady = (20, 0))

        # WIDGETS
        # Widgets - Buttons
        # Defining
        btn_back = ttk.Button(self.frm, text="Back",
                              command=lambda: back(self))

        # Placing
        btn_back.grid(row=2, column=4, sticky=E)
