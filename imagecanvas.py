from tkinter import *

root = Tk()
canvas=Canvas(root,height=700,width=666,bg="red")
canvas.pack()
photo=PhotoImage(file="L.gif")
img=canvas.create_image(0,0,image=photo,anchor=NW)
root.geometry("700x666+300+200")
root.resizable(0, 0)

mainloop()