from tkinter import *

root=Tk()
root.title("My Gui")
topfrmae=Frame(root,bg="White")
lbl=Label(topfrmae,text="enter your User Name",bg="red",fg="white",font=("Comic Sans Ms",12,"bold")).pack()
#lbl.pack()
btn=Button(topfrmae,text="click me")
btn.pack(side=TOP)

#bottomframe=Frame(root)
btn1=Button(topfrmae,text="click me1")
btn1.pack(fill=X)
#bottomframe.pack()

topfrmae.pack()

root.geometry("400x300+200+100")
mainloop()