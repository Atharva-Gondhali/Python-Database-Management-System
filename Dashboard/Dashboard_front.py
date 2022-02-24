from tkinter import *
from tkinter import ttk
from Dashboard.Dashboard_back import get_number_std
from Dashboard.Dashboard_back import get_number_crs
from Dashboard.Dashboard_back import get_best


class Dashboard:
    def __init__(self, frm):
        self.frm = frm

        # Label dashboard
        lbl_dash = ttk.Label(self.frm, text="Dashboard",
                             font=('Helvetica', 15))

        lbl_dash.grid(row=0, column=0, padx=30, pady=15,
                      sticky=W)

        # Frame
        frm1 = ttk.Frame(self.frm, width=300, height=220, padding=50)
        frm2 = ttk.Frame(self.frm, width=610, height=220, padding=(50, 30))
        frm3 = ttk.Frame(self.frm, width=300, height=220, padding=50)

        frm1.grid(row=1, column=0, padx=(10, 5), pady=(10, 5))
        frm2.grid(row=2, column=0, padx=(10, 5), pady=(10, 5),
                  columnspan=2)
        frm3.grid(row=1, column=1, padx=(10, 5), pady=(10, 5))

        frm1.grid_propagate(0)
        frm2.grid_propagate(0)
        frm3.grid_propagate(0)

        # Frame1
        lbl_std = ttk.Label(frm1, text="Students Admitted",
                            font=('Helvetica', 14))
        lbl_std_no = ttk.Label(
            frm1, text=get_number_std(),  font=('Helvetica', 14))

        lbl_std.grid(row=0, column=0, padx=20, pady=10)
        lbl_std_no.grid(row=2, column=0, padx=20, pady=10)

        # Frame2
        lbl_crs = ttk.Label(frm3, text="Courses Online",
                            font=('Helvetica', 14))
        lbl_crs_no = ttk.Label(
            frm3, text=get_number_crs(),  font=('Helvetica', 14))

        lbl_crs.grid(row=0, column=0, padx=20, pady=10)
        lbl_crs_no.grid(row=2, column=0, padx=20, pady=10)

        std = get_best()
        if std == None:
            std = ['', '', '']

        # Frame3
        lbl_best = ttk.Label(frm2, text="Best Performers",
                             font=('Helvetica', 14))
        lbl_p1 = ttk.Label(frm2, text="1st",
                           font=('Helvetica', 12))
        lbl_p2 = ttk.Label(frm2, text="2nd",
                           font=('Helvetica', 12))
        lbl_p3 = ttk.Label(frm2, text="3rd",
                           font=('Helvetica', 12))
        lbl_1 = ttk.Label(frm2, text=std[0],
                          font=('Helvetica', 12))
        lbl_2 = ttk.Label(frm2, text=std[1],
                          font=('Helvetica', 12))
        lbl_3 = ttk.Label(frm2, text=std[2],
                          font=('Helvetica', 12))

        lbl_best.grid(row=0, column=0, padx=20, pady=10)
        lbl_p1.grid(row=1, column=0, padx=25, pady=10,
                    sticky=NSEW)
        lbl_p2.grid(row=1, column=1, padx=25, pady=10,
                    sticky=NSEW)
        lbl_p3.grid(row=1, column=2, padx=25, pady=10,
                    sticky=NSEW)
        lbl_1.grid(row=2, column=0, padx=25, pady=10)
        lbl_2.grid(row=2, column=1, padx=25, pady=10)
        lbl_3.grid(row=2, column=2, padx=25, pady=10)
