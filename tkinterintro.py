from tkinter import *

root=Tk()
root.title("My Gui")
lbl=Label(root,text="enter your User Name",bg="red",fg="white",font=("Comic Sans Ms",12,"bold"))
lbl.pack()
btn=Button(root,text="click me")
btn.pack(side=LEFT)

btn1=Button(root,text="click me1")
btn1.pack(side=RIGHT)
root.geometry("400x300+200+100")
mainloop()