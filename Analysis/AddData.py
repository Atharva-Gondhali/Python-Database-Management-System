# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports


class AddData:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)

        # FUNCTIONS
        def back(cls):     # Back Function to go back a menu
            for widget in self.frm.winfo_children():
                widget.destroy()
            cls.frm.destroy()

        def callback(p):  # To validate some entry box to an integer input
            if str.isdigit(p) or p == "":
                return True
            else:
                return False


        # Widgets - Labels
        # Defining
        lbl_add_std = ttk.Label(self.frm, text="Add-Update Data",
                                font=('Helvetica', 15))
        lbl_sel_std = ttk.Label(self.frm, text="Select Student",
                                font=('Helvetica', 14))
        lbl_std_id = ttk.Label(self.frm, text="Student's ID No.",
                               font=('Helvetica', 11))
        lbl_std_det = ttk.Label(self.frm, text="Student details",
                                 font=('Helvetica', 14))
        lbl_std_name = ttk.Label(self.frm, text="Name",
                               font=('Helvetica', 11))
        lbl_std_course = ttk.Label(self.frm, text="Course",
                               font=('Helvetica', 11))
        lbl_std_ag = ttk.Label(self.frm, text="Age Group",
                               font=('Helvetica', 11))
        lbl_std_data = ttk.Label(self.frm, text="Student Data",
                                 font=('Helvetica', 14))
        lbl_spt = ttk.Label(self.frm, text="Sprint Test",
                               font=('Helvetica', 11))
        lbl_yt = ttk.Label(self.frm, text="Yoyo Test",
                               font=('Helvetica', 11))
        lbl_wt = ttk.Label(self.frm, text="Weight Sust Test",
                               font=('Helvetica', 11))
        lbl_stt = ttk.Label(self.frm, text="Stamina Test",
                               font=('Helvetica', 11))                       
        
        # Placing
        lbl_add_std.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)
        lbl_sel_std.grid(row=1, column=0, padx=30, pady=15,
                         sticky=W)
        lbl_std_id.grid(row=2, column=0, padx=30,
                        sticky=W)
        lbl_std_det.grid(row=3, column=0, padx=30, pady=15,
                          sticky=W)
        lbl_std_name.grid(row=4, column=0, padx=30, pady=5,
                        sticky=W)
        lbl_std_course.grid(row=5, column=0, padx=30, pady=5,
                        sticky=W)
        lbl_std_ag.grid(row=6, column=0, padx=30, pady=5,
                        sticky=W)
        lbl_std_data.grid(row=7, column=0, padx=30, pady=15,
                          sticky=W)
        lbl_spt.grid(row=8, column=0, padx=30, pady=5,
                        sticky=W)
        lbl_yt.grid(row=9, column=0, padx=30, pady=5,
                        sticky=W)
        lbl_wt.grid(row=10, column=0, padx=30, pady=5,
                        sticky=W)
        lbl_stt.grid(row=11, column=0, padx=30, pady=5,
                        sticky=W)
        # Widgets - Entry box
        v_cmd = (self.frm.register(callback))  # Validation for
        # integer input
        # Defining
        ent_std_id = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(v_cmd, '%P'))
        ent_std_name = ttk.Entry(self.frm, width=30, state='readonly')
        ent_std_course = ttk.Entry(self.frm, width=30, state='readonly')
        ent_std_ag = ttk.Entry(self.frm, width=30, state='readonly')
        ent_spt = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(v_cmd, '%P'))
        ent_yt = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(v_cmd, '%P'))
        ent_wt = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(v_cmd, '%P'))
        ent_stt = ttk.Entry(self.frm, width=30, validate='all',
                               validatecommand=(v_cmd, '%P'))
        # Placing
        ent_std_id.grid(row=2, column=1, padx=15)
        ent_std_name.grid(row=4, column=1, padx=15)
        ent_std_course.grid(row=5, column=1, padx=15)
        ent_std_ag.grid(row=6, column=1, padx=15)
        ent_spt.grid(row=8, column=1, padx=15)
        ent_yt.grid(row=9, column=1, padx=15)
        ent_wt.grid(row=10, column=1, padx=15)
        ent_stt.grid(row=11, column=1, padx=15)
        
        # Widgets - Buttons
        # Defining
        btn_select = ttk.Button(self.frm, text="Select", width=15)
        btn_update = ttk.Button(self.frm, text="Update", width=13)
        btn_back = ttk.Button(self.frm, text="Back", width=13,
                              command=lambda: back(self))

        # Placing
        btn_select.grid(row=2, column=2, sticky=W)
        btn_update.grid(row=12, column=2, padx=10, 
                        sticky=W, pady=10)
        btn_back.grid(row=12, column=3, pady=10)