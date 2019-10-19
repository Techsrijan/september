from tkinter import *
from tkinter import filedialog

def open_file():
    res=filedialog.askopenfile(initialdir="/",title="Select File to Open",filetype=(("Text File","*.txt"),("All File","*.*")))
    print(res)
    for data in res:
        print(data)

def save_file():
    f = filedialog.asksaveasfile(mode='w', defaultextension="*.txt")

root=Tk()
root.title("My Notepad")                                        #title name
root.wm_iconbitmap("notepad.ico")   #to add icon
btn=Button(root,text="click me",command=open_file)
btn.pack()


btn=Button(root,text="Save file",command=save_file)
btn.pack()

mainloop()