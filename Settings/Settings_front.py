from tkinter import *
from tkinter import ttk
from Settings.ChnPassword import ChnPassword
from Settings.Settings_back import delete_user


class Settings:
    def __init__(self, frm, main_frame, user):
        self.frm = frm

        def logout():
            main_frame.destroy()

        def delete():
            delete_user(user)
            logout()

        def chn_pass():
            frame_chn_pass = ttk.Frame(self.frm, width=635, height=535)
            ChnPassword(frame_chn_pass, user)

        lbl_settings = ttk.Label(self.frm, text="Settings",
                                 font=('Helvetica', 15))

        lbl_settings.grid(row=0, column=0, padx=30, pady=15,
                          sticky=W)

        btn_chn_pass = ttk.Button(self.frm, text="Change Password",
                                  width=20, command=chn_pass)
        btn_del_usr = ttk.Button(self.frm, text="Delete Account",
                                 width=20, command=delete)
        btn_logout = ttk.Button(self.frm, text="Logout",
                                width=20, command=logout)

        btn_chn_pass.grid(row=1, column=0, padx=50, pady=(30, 15),
                          ipady=8)
        btn_del_usr.grid(row=2, column=0, padx=50, pady=15,
                         ipady=8)
        btn_logout.grid(row=3, column=0, padx=50, pady=15,
                        ipady=8)
