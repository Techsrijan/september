from tkinter import *




root=Tk()
root.title("Note Pad")

def msg():
    print("File opened")


main_menu=Menu(root)
root.config(menu=main_menu)

# Create File Menu
filemenu=Menu(main_menu)
main_menu.add_cascade(label="File",menu=filemenu)

# to add menu inside file menu
filemenu.add_command(label="New Project    Ctrl+O",command=msg)
filemenu.add_command(label="Open Project")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)



# Create Edit Menu
editemenu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=editemenu)

root.geometry("500x300+300+200")
root.resizable(0,0)


mainloop()