from tkinter import *
from tkinter import filedialog,messagebox,colorchooser

root = Tk()
class Note:
    file=txt=w=w2=w3=u=j=None
    current_file = "no-file"
    def __init__(self,master):
        file=master
        master.title("Notepad-Untitled")
        master.wm_iconbitmap("notepad.ico")
        master.geometry("500x500+400+100")
        master.bind("<Alt-n>",self.new)
        master.bind("<Alt-o>", self.open)
        master.bind("<Alt-s>", self.saveas)
        master.bind("<Alt-p>", self.print)
        master.bind("<Alt-c>", self.copy)
        master.bind("<Alt-x>", self.cut)
        master.bind("<Alt-v>", self.paste)
        master.bind("<Alt-a>", self.sa)
        self.outermenu=Menu(master)
        master.config(menu=self.outermenu)
        self.txt = Text(master,width=20,height=3,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="red")
        self.txt.pack(fill=BOTH, expand=1)

        self.filem=Menu(self.outermenu,tearoff=0)
        self.outermenu.add_cascade(label="File",menu=self.filem)

        self.filem.add_command(label="New     Alt+n",command=self.new)
        self.filem.add_command(label="Open    Alt+o",command=self.open)
        self.filem.add_command(label="Save    Alt+s",command=self.save)
        self.filem.add_command(label="SaveAs  Alt+s ",command=self.saveas)
        self.filem.add_separator()
        self.filem.add_command(label="PageSetup")
        self.filem.add_command(label="Print   Alt+p",command=self.print)
        self.filem.add_separator()
        self.filem.add_command(label="Exit",command=master.destroy)

        self.editm=Menu(self.outermenu,tearoff=0)
        self.outermenu.add_cascade(menu=self.editm,label="Edit")
        self.editm.add_command(label="Undo   Alt+z",command=self.txt.edit_undo)
        self.editm.add_command(label="Redo   Alt+y", command=self.txt.edit_redo)
        self.editm.add_separator()
        self.editm.add_command(label="Cut     Alt+x",command=self.cut)
        self.editm.add_command(label="Copy    Alt+c",command=self.copy)
        self.editm.add_command(label="Paste   Alt+v",command=self.paste)
        self.editm.add_command(label="Delete    del",command=self.delete)
        self.editm.add_separator()
        self.editm.add_command(label="Find    Alt+f")
        self.editm.add_command(label="FindNext")
        self.editm.add_command(label="Replace   Alt+h")
        self.editm.add_command(label="GoTo     Alt+g")
        self.editm.add_separator()
        self.editm.add_command(label="SelectAll  Alt+a",command=self.sa)
        self.editm.add_command(label="Time/Date")

        self.formatm=Menu(self.outermenu,tearoff=0)
        self.outermenu.add_cascade(menu=self.formatm,label="Format")
        self.formatm.add_command(label="WordWrap")
        self.formatm.add_command(label="Font")

        self.viewm = Menu(self.outermenu,tearoff=0)
        self.outermenu.add_cascade(menu=self.viewm, label="Format")
        self.viewm.add_command(label="Status")

        self.helpm = Menu(self.outermenu,tearoff=0)
        self.outermenu.add_cascade(menu=self.helpm, label="Help")
        self.helpm.add_command(label="ViewHelp")
        self.helpm.add_separator()
        self.helpm.add_command(label="About Notebook")

    def new(self,event=""):
        s = self.txt.get(1.0, END)
        if not s.strip():
            pass
        else:
            result = messagebox.askyesnocancel("Save Dialog box", "Do you want to save this file?")
            if result == True:
                self.saveas()
                self.clear()
            elif result == False:
                self.clear()

    def open(self,event=""):
        res = filedialog.askopenfile(initialdir="/", title="Select File to Open",
                                     filetype=(("Text File", "*.txt"), ("All File", "*.*")))
        #print(res)
        for data in res:
            self.txt.insert(INSERT, data)
        self.current_file = res.name

    def save(self, event=""):
        if self.current_file == "no-file":
            self.saveas()
        else:
            f = open(self.current_file, mode="w")
            f.write(self.txt.get(1.0, END))
            f.close()

    def clear(self):
        self.txt.delete(1.0, END)

    def saveas(self, event=""):
        f = filedialog.asksaveasfile(mode='w', defaultextension="*.txt")
        data = self.txt.get(1.0, END)
        f.write(data)
        self.current_file = f.name
        f.close()

    def print(self,event=""):
        g=self.txt.get(1.0,END)
        print(g)

    ''' def cut(self,event=""):
        self.u="cut"
        self.w=self.txt.selection_get()
        i=self.txt.search(self.w,1.0,END)
        l=int(i.split('.')[1])+len(self.w)
        e=i.split('.')[0]+"."+str(l)
        self.j=i
        self.txt.delete(i,e)

    def copy(self,event=""):
        self.u = "copy"
        self.w=self.txt.selection_get()
    '''
    def delete(self,event=""):
        self.u = "delete"
        self.w2=self.txt.selection_get()
        i=self.txt.search(self.w2,1.0,END)
        l=int(i.split('.')[1])+len(self.w2)
        e=i.split('.')[0]+"."+str(l)
        self.j=i
        self.txt.delete(i,e)

    '''def paste(self,event=""):
        self.u = "paste"
        self.w2=self.txt.selection_get()
        i=self.txt.search(self.w2,1.0,END)
        l=int(i.split('.')[1])+len(self.w2)
        e=i.split('.')[0]+"."+str(l)
        self.txt.delete(i,e)
        self.txt.insert(INSERT,self.w,i)'''

    def cut(self):
        self.copy()
        self.txt.delete('sel.first', 'sel.last')
    def copy(self):
        self.txt.clipboard_clear()
        self.txt.clipboard_append(self.txt.selection_get())
    def paste(self):
        self.txt.insert(INSERT, self.txt.clipboard_get())




    def sa(self,event=""):
        self.u = "sa"
        self.w= self.txt.get(0.0,END)
        print(self.w)

    '''def undo(self,event=""):
        if self.u=="cut":
            self.txt.insert(INSERT,self.w,self.j)
        if self.u=="delete" or self.u=="paste":
            self.txt.insert(INSERT, self.w2, self.j)'''


n=Note(root)

mainloop()


