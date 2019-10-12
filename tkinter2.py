from tkinter import *

def msg():
    print("Good day")

root=Tk()
root.title("My Gui")
lbl=Label(root,text="enter your User Name",bg="red",fg="white",font=("Comic Sans Ms",12,"bold"))
lbl.place(x=10,y=20)
btn=Button(root,text="click me")
btn.place(x=300,y=20)

btn1=Button(root,text="click me1",command=msg)
btn1.pack(side=RIGHT)
root.geometry("400x300+200+100")
mainloop()