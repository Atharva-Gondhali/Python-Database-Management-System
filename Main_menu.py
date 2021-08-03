from tkinter import ttk
from Main_workspace import Workspace


class Menu:
    def __init__(self, main_frame, frm, frm_work, user):
        self.frm = frm
        self.frm_work = frm_work
        self.main_frm = main_frame
        self.frm.grid(row=1, column=0, padx=(15, 10), pady=(10, 15))
        self.frm.grid_propagate(0)

        frm_workspace = Workspace(frm_work)

        # Functions Menu -
        def open_menu_items(frame):
            if frame == "Dashboard":
                frm_workspace.change_dash()

            elif frame == "Student":
                frm_workspace.change_std()

            elif frame == "Settings":
                frm_workspace.change_set(main_frame, user)

        # STYLES
        style = ttk.Style()
        style.configure('menu.TButton', font=('Helvetica', 10),
                        width=22)
        style.configure('heading_text.TButton', font=('Helvetica', 15))

        # Buttons Menu
        btn_dash = ttk.Button(self.frm, text="Dashboard",
                              style='menu.TButton',
                              command=lambda: open_menu_items("Dashboard"))
        btn_student = ttk.Button(self.frm, text="Students",
                                 style='menu.TButton',
                                 command=lambda: open_menu_items("Student"))
        btn_unknown1 = ttk.Button(self.frm, text=".........",
                                  style='menu.TButton')
        btn_unknown2 = ttk.Button(self.frm, text=".........",
                                  style='menu.TButton')
        btn_settings = ttk.Button(self.frm, text="Settings",
                                  style='menu.TButton',
                                  command = lambda: open_menu_items("Settings"))

        btn_dash.grid(row=0, column=0, ipady=23)
        btn_student.grid(row=1, column=0, ipady=23, pady=(10, 0))
        btn_unknown1.grid(row=2, column=0, ipady=23, pady=(10, 0))
        btn_unknown2.grid(row=3, column=0, ipady=23, pady=(10, 0))
        btn_settings.grid(row=4, column=0, ipady=23, pady=(10, 0))

        # Label menu
        lbl_logo = ttk.Label(self.frm, text="logo/app name")

        lbl_logo.grid(row=5, column=0, pady=(30, 0))
