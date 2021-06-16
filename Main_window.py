# IMPORTS
from tkinter import ttk

from Main_menu import *


class Main:
    def __init__(self, win):
        self.win = win
        self.win.geometry("915x665")
        self.win.resizable(width=False, height=False)

        main_frame = ttk.Frame(self.win, width=895, height=660)
        menu_frame = ttk.Frame(main_frame, borderwidth=3,
                               relief=GROOVE, width=200, height=540, padding=15)
        workspace_frame = ttk.Frame(main_frame, borderwidth=3,
                                    relief=GROOVE, width=640, height=540)
        account_frame = ttk.Frame(main_frame, borderwidth=3,
                                  relief=GROOVE, height=65)

        # main_frame.grid_propagate(0)
        account_frame.grid_propagate(0)

        main_frame.grid(row=0, column=0, padx=10, pady=10)
        account_frame.grid(row=0, column=0, padx=15, pady=(15, 0),
                           columnspan=2, sticky=EW)

        Menu(menu_frame, workspace_frame)