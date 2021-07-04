from tkinter import *
from tkinter import ttk
from time import strftime
from Main_menu import Menu


class Main:
    def __init__(self, win, user):
        self.user = user
        self.win = win
        self.win.geometry("915x665")
        self.win.resizable(width=False, height=False)


        def clock():
            day = strftime("%A")
            hour = strftime("%I")
            minute = strftime("%M")
            mer = strftime("%p")

            lbl_clock.configure(text=day + ', ' + hour +
                                ':' + minute + ' ' + mer)
            lbl_clock.after(1000, clock)


        main_frame = ttk.Frame(self.win, width=895, height=660)
        menu_frame = ttk.Frame(main_frame, borderwidth=3,
                               relief=GROOVE, width=200,
                               height=540, padding=15)
        workspace_frame = ttk.Frame(main_frame, borderwidth=3,
                                    relief=GROOVE, width=640,
                                    height=540)
        account_frame = ttk.Frame(main_frame, borderwidth=3,
                                  relief=GROOVE, height=65)

        # main_frame.grid_propagate(0)
        account_frame.pack_propagate(0)

        main_frame.grid(row=0, column=0, padx=10, pady=10)
        account_frame.grid(row=0, column=0, padx=15, pady=(15, 0),
                           columnspan=2, sticky=EW)


        lbl_clock = ttk.Label(account_frame, text="",
                              font=('Helvetica', 10))
        lbl_user = ttk.Label(account_frame, text=self.user,
                             font=('Helvetica', 16))

        lbl_user.pack(anchor=E, padx=(0, 10))
        lbl_clock.pack(anchor=E, padx=(0, 10))

        clock()

        Menu(menu_frame, workspace_frame)
