from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x300")

def get():
    text.insert('1.0', textstr, END)

textstr = 'asdfsadfsadf\nasfasd\nfsadfsdafasdfsadfsdafsdfas'  

btn = ttk.Button(root, text = "change", command = get)
btn.grid(row = 0, column = 0, padx = 10, pady = 10)

text = Text(root, height = 10, width = 20, font = ('Helvetica', 12))
text.grid(row = 1, column = 0, padx = 10, pady = 10)

root.mainloop()