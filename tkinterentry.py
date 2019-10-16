from tkinter import *

def msg():
    print("Good day")
    print(s.get())
    a=s2.get()+s.get()
    print(a)

root=Tk()
root.title("My Gui")
lbl=Label(root,text="enter your User Name",bg="red",fg="white",font=("Comic Sans Ms",12,"bold"))
lbl.place(x=10,y=20)

s=IntVar()
e=Entry(root,bg="red",show="*",fg="white",font=("Comic Sans Ms",12,"bold"),textvariable=s)
e.place(x=300,y=20)

s2=IntVar()
e2=Entry(root,bg="red",bd=20,justify="right",insertwidth=40,fg="white",font=("Comic Sans Ms",12,"bold"),textvariable=s2)
e2.place(x=300,y=150)


btn=Button(root,text="click me",command=msg)
btn.place(x=300,y=50)

btn1=Button(root,text="click me1")
btn1.pack(side=RIGHT)
root.geometry("600x300+200+100")
#root.resizable(0,0)
mainloop()