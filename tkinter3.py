from tkinter import *

def msg(event):
    print("Good day")


def msg2(event):
    print("Good afternoon")

def msg3(event):
    print("Good Evening")


root=Tk()
root.title("My Gui")
lbl=Label(root,text="enter your User Name",bg="red",fg="white",font=("Comic Sans Ms",12,"bold"))
lbl.place(x=10,y=20)

root.bind("<Button-1>",msg)
root.bind("<Button-2>",msg2)
root.bind("<Button-3>",msg3)

btn=Button(root,text="Right Click")
btn.pack()

btn1=Button(root,text="Middle click")
btn1.pack()

btn2=Button(root,text="Left Click")
btn2.pack()

root.geometry("400x300+200+100")
mainloop()