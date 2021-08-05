from tkinter import *
from tkinter import ttk
from Settings.Settings_back import verify_password, \
    change_password

class ChnPassword:
    def __init__(self, frm, user):
        self.frm = frm  
        self.frm.grid_propagate(0)
        self.frm.grid(row=0, column=0)


        def back(self):
            self.frm.destroy()

        def clear():
            for i in [ent_cur_pass, ent_new_pass, ent_cnew_pass]:
                i.delete(0, END)

        def change_war_state(state):
            lbl_var_pass.configure(foreground = state)
            lbl_inc_pass.configure(foreground = state)

        def change_state(state):
            ent_new_pass.configure(state = state)
            ent_cnew_pass.configure(state = state)
            btn_new_pass.configure(state = state)

        def check_pass(paswd):
            if verify_password(user, paswd):
                change_state('normal')
                change_war_state('white')
            else:
                lbl_inc_pass.configure(foreground= 'black')
                change_state('disable')

        def set_pass(passwd, cpasswd):
            if passwd == cpasswd:
                change_password(user, passwd)
                clear()
                change_war_state('white')
                change_state('disabled')
            else:
                lbl_var_pass.configure(foreground= 'black')


        lbl_chn_pass = ttk.Label(self.frm, text="Change Password",
                                font=('Helvetica', 15))
        lbl_cur_pass = ttk.Label(self.frm, text="Current password",
                                 font=('Helvetica', 12))
        lbl_inc_pass = ttk.Label(self.frm, text="Incorrect Password.",
                                 font=('Helvetica', 10), 
                                 foreground = 'white')
        lbl_new_pass = ttk.Label(self.frm, text="New password",
                                 font=('Helvetica', 12))
        lbl_cnew_pass = ttk.Label(self.frm, text="Confirm New password",
                                 font=('Helvetica', 12))
        lbl_var_pass = ttk.Label(self.frm, text="Passwords do not match.",
                                 font=('Helvetica', 10), 
                                 foreground = 'white')

        lbl_chn_pass.grid(row=0, column=0, padx=30, pady=15,
                         sticky=W)
        lbl_cur_pass.grid(row = 1, column = 0, padx=30, 
                          pady = (15, 10), sticky = W)
        lbl_inc_pass.grid(row = 3, column = 0, sticky = E, 
                          columnspan = 2)
        lbl_new_pass.grid(row = 4, column = 0, padx=30, 
                          pady = (15, 10), sticky = W)
        lbl_cnew_pass.grid(row = 6, column = 0, padx=30, 
                          pady = (30, 10), sticky = W)
        lbl_var_pass.grid(row = 8, column = 0, sticky = E, 
                          columnspan = 2)


        btn_cur_pass = ttk.Button(self.frm, text = "Enter", 
                                  width = 15, 
                                command= lambda: check_pass(ent_cur_pass.get()))
        btn_new_pass = ttk.Button(self.frm, text = "Change", 
                                  width = 15, state = 'disabled',
                                  command = lambda: set_pass(ent_new_pass.get(), 
                                                             ent_cnew_pass.get()))
        btn_back = ttk.Button(self.frm, text = "Back", 
                              width = 15,
                              command=lambda: back(self))

        btn_cur_pass.grid(row = 2, column = 1, padx = 10, 
                          pady = (15, 10))
        btn_new_pass.grid(row = 7, column = 1, padx = 10, 
                          pady = (15, 10))
        btn_back.grid(row = 8, column = 2, padx = 70, 
                          pady = (70, 0))


        ent_cur_pass = ttk.Entry(self.frm, width = 28)
        ent_new_pass = ttk.Entry(self.frm, width = 28, 
                                 state = 'disabled')
        ent_cnew_pass = ttk.Entry(self.frm, width = 28, 
                                  state = 'disabled')

        ent_cur_pass.grid(row = 2, column = 0, padx=(40, 10), 
                          pady = (5, 0))
        ent_new_pass.grid(row = 5, column = 0, padx=(40, 10), 
                                  pady = (5, 0))
        ent_cnew_pass.grid(row = 7, column = 0, padx=(40, 10), 
                          pady = (5, 0))
                          