from tkinter import *

def msg(event=""):
    print("Good day")

root=Tk()
root.title("My Gui")
root.bind("<Control-m>",msg)

btn=Button(root,text="Right Click",command=msg)
btn.pack()
root.geometry("400x300+200+100")
mainloop()