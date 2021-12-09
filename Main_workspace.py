from Course.Course_front import Course
from Dashboard_front import Dashboard
from Settings.Settings_front import Settings
from Student.Student_front import Student


class Workspace:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid(row=1, column=1, padx=(10, 15), pady=(10, 15))
        self.frm.grid_propagate(0)

        Dashboard(self.frm)

    def change_dash(self):
        for widgets in self.frm.winfo_children():
            widgets.destroy()
        Dashboard(self.frm)

    def change_std(self):
        for widgets in self.frm.winfo_children():
            widgets.destroy()
        Student(self.frm)

    def change_cor(self):
        for widgets in self.frm.winfo_children():
            widgets.destroy()
        Course(self.frm)

    def change_set(self, main_frame, user):
        for widgets in self.frm.winfo_children():
            widgets.destroy()
        Settings(self.frm, main_frame, user)
