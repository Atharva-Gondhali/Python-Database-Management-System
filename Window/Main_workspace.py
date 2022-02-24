from Dashboard.Dashboard_front import Dashboard
from Student.Student_front import Student
from Course.Course_front import Course
from Analysis.Analysis_front import Analysis
from Settings.Settings_front import Settings


class Workspace:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid(row=1, column=1, padx=(10, 15), pady=(10, 15))
        self.frm.grid_propagate(0)

        Dashboard(self.frm)

    def change_dash(self):
        for widget in self.frm.winfo_children():
            widget.destroy()
        Dashboard(self.frm)

    def change_std(self):
        for widget in self.frm.winfo_children():
            widget.destroy()
        Student(self.frm)

    def change_cor(self):
        for widget in self.frm.winfo_children():
            widget.destroy()
        Course(self.frm)
    
    def change_ana(self):
        for widget in self.frm.winfo_children():
            widget.destroy()
        Analysis(self.frm)

    def change_set(self, main_frame, user):
        for widget in self.frm.winfo_children():
            widget.destroy()
        Settings(self.frm, main_frame, user)
