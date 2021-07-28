from tkinter import *
from tkinter import ttk

class Settings:
    def __init__(self, frm):
        self.frm = frm


        lbl_settings = ttk.Label(self.frm, text="Settings",
                                font=('Helvetica', 15))

        lbl_settings.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)

        btn_chn_pass = ttk.Button(self.frm, text = "Change Password",
                                  width = 20)
        btn_del_usr = ttk.Button(self.frm, text = "Delete User",
                                  width = 20)
        btn_logout = ttk.Button(self.frm, text = "Logout",
                                  width = 20)

        btn_chn_pass.grid(row = 1, column = 0, padx=50, pady=(30, 15),
                          ipady=8 )
        btn_del_usr.grid(row = 2, column = 0, padx=50, pady=15,
                          ipady=8 )
        btn_logout.grid(row = 3, column = 0, padx=50, pady=15,
                          ipady=8 )