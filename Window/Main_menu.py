from tkinter import ttk
from Window.Main_workspace import Workspace


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
            elif frame == "Course":
                frm_workspace.change_cor()
            elif frame == "Analysis":
                frm_workspace.change_ana()
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
        btn_student = ttk.Button(self.frm, text="    Student\nManagement",
                                 style='menu.TButton',
                                 command=lambda: open_menu_items("Student"))
        btn_course = ttk.Button(self.frm, text="    Course\nManagement",
                                style='menu.TButton',
                                command=lambda: open_menu_items("Course"))
        btn_analysis = ttk.Button(self.frm, text="Physical\nAnalysis",
                                  style='menu.TButton',
                                  command=lambda: open_menu_items("Analysis"))
        btn_settings = ttk.Button(self.frm, text="Settings",
                                  style='menu.TButton',
                                  command=lambda: open_menu_items("Settings"))

        btn_dash.grid(row=0, column=0, ipady=23)
        btn_student.grid(row=1, column=0, ipady=16, pady=(10, 0))
        btn_course.grid(row=2, column=0, ipady=16, pady=(10, 0))
        btn_analysis.grid(row=3, column=0, ipady=16, pady=(10, 0))
        btn_settings.grid(row=4, column=0, ipady=23, pady=(10, 0))

        # Label menu
        lbl_logo = ttk.Label(self.frm, text="SCMS", font = ('Helvetica', 15))

        lbl_logo.grid(row=5, column=0, pady=(30, 0))
