from tkinter import *

root = Tk()
root.geometry( "400x400" )

lbl1 = Label( root, text = "Hello" )
lbl2 = Label( root, text = "World" )

lbl1.grid( row = 0, column = 0, padx = 10, pady = 10 )
lbl2.grid( row = 0, column = 0, padx = 10, pady = 10 )

def Test():
        lbl2.destroy()

btn = Button( root, text = "Test", command = Test )
btn.grid( row = 1, column = 0, padx = 10, pady = 10 )

root.mainloop()