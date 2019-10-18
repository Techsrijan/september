from tkinter import *


class Gui:
    def __init__(self,master):
        self.printButton=Button(master,text="Print",bg="red",command=self.msg)
        self.printButton.pack()
        self.closeButton = Button(master, text="Close", bg="red", command=quit)
        self.closeButton.pack()


    def msg(self):
        print("hi")






root=Tk()
b=Gui(root)
mainloop()