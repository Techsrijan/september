from tkinter import *

def msg():
    s=l.curselection()
    for item in s:
        print(l.get(item))
    print(s)
    
def msg1():
    s = l.curselection()
    for item in s:
        print(l.delete(item))

root=Tk()
root.title("Login form")

l=Listbox(root,width=30,height=15,selectmode=SINGLE)
l.insert(1,"Java")
l.insert(2,"Python")
l.insert(3,"Java")
l.insert(4,"Python")
l.insert(5,"Java")
l.insert(6,"Python")
l.pack()

btn=Button(root,text="Login",fg="white",bg="red",bd=10,font=("Times", "24", "bold italic"),command=msg).pack()

btn1=Button(root,text="Delete",fg="white",bg="red",bd=10,font=("Times", "24", "bold italic"),command=msg1).pack()

root.geometry("700x666+300+200")
root.resizable(0,0)


mainloop()