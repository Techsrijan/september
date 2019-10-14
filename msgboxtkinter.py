from tkinter import *
from tkinter import messagebox
root=Tk()

def openmsg():
   messagebox.showwarning("Success","Transaction completed")

def save():
    ans=messagebox.askquestion("Save |File ","Do U want to save file?")
    #ans=messagebox.askyesnocancel("Save |File ","Do U want to save file?")
    print(ans)
    if ans=="yes":
        print("File Saveed suceesfully")
    else:
        pass


btn=Button(root,text="click me",command=openmsg)
btn.place(x=300,y=50)

btn1=Button(root,text="Save",command=save)
btn1.place(x=300,y=100)

btn2=Button(root,text="Quit",command=quit)
btn2.place(x=300,y=150)
root.geometry("400x300+200+100")
mainloop()