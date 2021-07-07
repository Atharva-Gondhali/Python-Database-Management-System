from tkinter import *
from tkinter import ttk
from Student.Widgets import Widgets


class SearchStudent:
    def __init__(self, frm, tpl):
        self.tpl = tpl
        self.frm = frm
        self.frm.grid_propagate(0)
        self.frm.grid(row=0, column=0)


        def back(self):
            self.frm.destroy()


        def widgets(self):
            self.lbl_father_name.grid(row=1, column=1, padx=(40, 5),
                                      pady=(20, 5), sticky = W)
            self.lbl_email_id.grid(row=3, column=0, padx=(30, 40), pady=(15, 5),
                                   sticky=W)
            self.lbl_age.grid(row = 3, column=1, padx=(40, 5),
                              pady=(15, 5), sticky = W)
            self.lbl_age_group.grid(row=5, column=0, padx=(30, 40), pady=(15, 5),
                                    sticky=W)
            self.lbl_gender.grid(row=5, column=1, padx=(40, 5),
                                 pady=(15, 5), sticky = W)
            self.lbl_course.grid(row=7, column=0, padx=(30, 40), pady=(15, 5),
                                 sticky=W)
            self.lbl_medical_com.grid(row=7, column=1, padx=(40, 5),
                                      pady=(15, 5), sticky = W)
            self.lbl_address.grid(row=9, column=0, padx=(30, 40), pady=(15, 5),
                                  sticky=W)
            self.lbl_phone_number.grid(row=9, column=1, padx=(40, 5),
                                       pady=(15, 0), sticky=W)

        wdg = Widgets(self.frm)
        lbl_heading = ttk.Label(self.frm, text = "Search Student", 
                                font = ('Helvetica', 14))
        lbl_student = ttk.Label(self.frm, text = "Student", 
                                font = ('Helvetica', 11))
        lbl_student_val = ttk.Label(self.frm, 
                                    text = self.tpl[1]+' '+self.tpl[2], 
                                font = ('Helvetica', 13))
        lbl_father = ttk.Label(self.frm, text = self.tpl[3], 
                                font = ('Helvetica', 13))
        lbl_email = ttk.Label(self.frm, text = self.tpl[4], 
                                font = ('Helvetica', 13))
        lbl_age = ttk.Label(self.frm, text = self.tpl[5], 
                                font = ('Helvetica', 13))
        lbl_agegroup = ttk.Label(self.frm, text = self.tpl[6], 
                                font = ('Helvetica', 13))                                
        lbl_gender = ttk.Label(self.frm, text = self.tpl[7], 
                                font = ('Helvetica', 13))
        lbl_course = ttk.Label(self.frm, text = self.tpl[8], 
                                font = ('Helvetica', 13))
        lbl_medical = ttk.Label(self.frm, text = self.tpl[9], 
                                font = ('Helvetica', 13))   
        lbl_address = ttk.Label(self.frm, text = self.tpl[10], 
                                font = ('Helvetica', 13))                             
        lbl_phone = ttk.Label(self.frm, text = self.tpl[11], 
                                font = ('Helvetica', 13))
        

        lbl_heading.grid(row = 0, column = 0, padx=30, pady=15,
                         sticky=W, columnspan = 2)
        lbl_student.grid(row = 1, column = 0, padx=30, pady = (20,5), 
                        sticky = W)
        lbl_student_val.grid(row=2, column=0, padx=(30, 5),
                        pady=5, sticky = W)
        lbl_father.grid(row=2, column=1, padx=(40, 5),
                        pady=5, sticky = W)
        lbl_email.grid(row=4, column=0, padx=(30, 40), pady=(5, 15),
                       sticky=W)
        lbl_age.grid(row = 4, column=1, padx=(40, 5),
                     pady=5, sticky = W)
        lbl_agegroup.grid(row=6, column=0, padx=(30, 40), pady=(5, 15),
                          sticky=W)
        lbl_gender.grid(row=6, column=1, padx=(40, 5),
                        pady=5, sticky = W)
        lbl_course.grid(row=8, column=0, padx=(30, 40), pady=(5, 15),
                        sticky=W)
        lbl_medical.grid(row=8, column=1, padx=(40, 5),
                        pady=5, sticky = W)
        lbl_address.grid(row=10, column=0, padx=(30, 40), pady=(5, 15),
                         sticky=W)
        lbl_phone.grid(row=10, column=1, padx=(40, 5),
                       pady=5, sticky=W)

        btn_back = ttk.Button(self.frm, text = "Back", 
                              command=lambda: back(self))

        btn_back.grid(row = 11, column = 2, padx = 10, pady = 10,
                      sticky = E, ipadx=6)

        widgets(wdg)
