from tkinter import *

root = Tk()
canvas=Canvas(root,height=200,width=200,bg="red")
canvas.pack()
l=canvas.create_line(0,0,100,100,fill="yellow",width=15)
c=canvas.create_rectangle(0,0,100,200,fill="blue")
o=canvas.create_oval(0,0,100,200,fill="yellow",width=4)
a=canvas.create_arc(0,0,100,200,extent=120,fill="green",width=4)

root.geometry("700x666+300+200")
root.resizable(0, 0)

mainloop()