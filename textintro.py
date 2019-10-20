from tkinter import *
from tkinter import filedialog,colorchooser
def msg():
    s=text1.get(1.0,END)
    print(s)

def selectedvalue():
    res=text1.selection_get()
    print(res)
    pos=text1.search(res,1.0,stopindex=END)
    print(pos)
def clear():
    text1.delete(1.0,END)


def open_file():
    res=filedialog.askopenfile(initialdir="/",title="Select File to Open",filetype=(("Text File","*.txt"),("All File","*.*")))
    print(res)
    for data in res:
        print(data)
        text1.insert(INSERT, data)

def save_file():
    f = filedialog.asksaveasfile(mode='w', defaultextension="*.txt")
    print(f)
    if f is None:
        return
    f.write("hello how r u")
    f.close()
def fore_color():
    c=colorchooser.askcolor()
    #text1.configure(foreground=c[1])
    text1.configure(background=c[1])
    print(c)

root=Tk()
root.title("My Notepad")                                        #title name
root.wm_iconbitmap("notepad.ico")   #to add icon

text1=Text(root,width=40,height=15,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="red")
text1.config(font=("Comic Sans Ms",12,"bold"))
text1.insert(INSERT,"Hello h ow r u?")
text1.pack()

btn=Button(root,text="click me",command=msg)
btn.pack()

btn1=Button(root,text="seleted text",command=selectedvalue)
btn1.pack()


btn2=Button(root,text="clear text",command=clear)
btn2.pack()

btn4=Button(root,text="open file",command=open_file)
btn4.pack()


btn5=Button(root,text="Save file",command=save_file)
btn5.pack()


btn6=Button(root,text="Fore Ground color",command=fore_color)
btn6.pack()
#text1.pack(fill=BOTH, expand=1)
mainloop()