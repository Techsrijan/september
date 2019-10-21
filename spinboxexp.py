from tkinter import *
from tkinter.ttk import Combobox
def comboget():
    print(c.get())

root = Tk()
c=Spinbox(root,from_=1,to=5)
c.pack()

d=Scale(root,from_=1,to=50,orient=HORIZONTAL,length=400,sliderlength=100,width=15)
d.set(25)
d.pack()

btn = Button(root, text="combodata",command=comboget).pack()
root.geometry("400x500+120+120")
root.resizable(0, 0)
mainloop()
