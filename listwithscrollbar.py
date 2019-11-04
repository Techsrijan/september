from tkinter import *

root = Tk()
frame=Frame(root)
root.title("Login form")
scroll=Scrollbar(frame)
l = Listbox(frame, width=30, height=15, selectmode=SINGLE)
for i in range(1,44):
    l.insert(END,"LIST"+str(i))

scroll.config(command=l.yview)
scroll.pack(side=RIGHT,fill=Y)
l.pack()
frame.pack()
root.geometry("700x666+300+200")
root.resizable(0, 0)

mainloop()