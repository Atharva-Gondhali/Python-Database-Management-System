# IMPORTS
from tkinter import *
from tkinter import ttk  # Tkinter imports

class CourseTest:
    def __init__(self, frm):
        self.frm = frm
        self.frm.grid_propagate(0)  # initializing frame and class
        self.frm.grid(row=0, column=0)