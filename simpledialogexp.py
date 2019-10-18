from tkinter import *
from tkinter import simpledialog

def msg():
    s=simpledialog.askstring("Input String Value","Please Enter your Name")
    print(s)


root=Tk()
root.title("Login form")


btn=Button(root,text="popup open",fg="white",bg="red",bd=10,font=("Times", "24", "bold"),command=msg).pack()
root.geometry("500x300+300+200")
root.resizable(0,0)


mainloop()