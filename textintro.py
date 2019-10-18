from tkinter import *
root=Tk()
root.title("My Notepad")                                        #title name
root.wm_iconbitmap("notepad.ico")   #to add icon

text1=Text(root,width=20,height=3,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="red")
text1.config(font=("Comic Sans Ms",20,"bold"))
text1.insert(INSERT,"Hello how r u?")
text1.pack()
#text1.pack(fill=BOTH, expand=1)
mainloop()