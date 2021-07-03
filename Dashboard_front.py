from tkinter import *
from tkinter import ttk


class Dashboard():
    def __init__(self, frm):
        self.frm = frm

        # Label dashboard
        lbl_dash = ttk.Label(self.frm, text="Dashboard",
                             font=('Helvetica', 15))

        lbl_dash.grid(row=0, column=0, padx=30, pady=15,
                      sticky=W)
