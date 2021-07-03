from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x300")

lst = ["Dell", "Lenovo", "Asus", "Acer", "HP"]

def update(event):
    values = []
    for i in lst:
        if combo.get() in i and combo.get() != '':
            values.append(i) 
    
    combo.configure(values = values )


combo = ttk.Combobox(root)
combo.grid(row = 0, column = 0, padx = 30, pady = 30)
combo.bind("<KeyRelease>", update)

root.mainloop()