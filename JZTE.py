from Tkinter import *
from PIL import Image, ImageTk


def nothing():
    print "a"










root = Tk()

#File Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Save", command=nothing)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#Zoom Menu
zoommenu = Menu(menubar, tearoff=0)
zoommenu.add_command(label="100%", command=nothing)
zoommenu.add_command(label="200%", command=nothing)
zoommenu.add_command(label="50%", command=nothing)

menubar.add_cascade(label="Zoom", menu=zoommenu)
root.config(menu=menubar)

image = Image.open("bold.png")
photo = ImageTk.PhotoImage(image)

#Buttons
boldbutton = Button(root, text="B", image=photo, command=nothing)
boldbutton.image = photo # keep a reference!
boldbutton.grid(row=0, column=0)





italicbutton = Button(root, text="I", command=nothing)
italicbutton.grid(row=0, column=1)


underlinebutton = Button(root, text="U", command=nothing)
underlinebutton.grid(row=0, column=2)





mainloop()