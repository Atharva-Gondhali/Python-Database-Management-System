# from tkinter import *
# from tkinter import ttk
from pickle import load

# root = Tk()
# root.geometry("500x300")

# isTextStar = True

# def change():
#     global isTextStar
#     if isTextStar:
#         ent.configure(show = '')
#         isTextStar = False
#     else:
#         ent.configure(show = '*')
#         isTextStar = True

# btn = ttk.Button(root, text = "change", command = change)
# ent = ttk.Entry(root, show = '*')

# btn.grid(row = 0, column = 0)
# ent.grid(row = 0, column = 1)

# root.mainloop()

file = open("logger.pkl", "rb")
info = load(file)
print(info)
