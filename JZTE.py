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
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

#Buttons
boldbutton = Button(root, text="B", image=photo, command=nothing)
boldbutton.image = photo # keep a reference!
boldbutton.grid(row=0, column=0)

image = Image.open("italic.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

italicbutton = Button(root, text="I", image=photo, command=nothing)
italicbutton.image = photo
italicbutton.grid(row=0, column=1)

image = Image.open("underline.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

underlinebutton = Button(root, text="U", image=photo, command=nothing)
underlinebutton.image = photo
underlinebutton.grid(row=0, column=2)

image = Image.open("left.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

leftbutton = Button(root, text="U", image=photo, command=nothing)
leftbutton.image = photo
leftbutton.grid(row=0, column=3)

image = Image.open("center.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

centerbutton = Button(root, text="U", image=photo, command=nothing)
centerbutton.image = photo
centerbutton.grid(row=0, column=4)

image = Image.open("right.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

rightbutton = Button(root, text="U", image=photo, command=nothing)
rightbutton.image = photo
rightbutton.grid(row=0, column=5)

image = Image.open("font.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

fontbutton = Button(root, text="U", image=photo, command=nothing)
fontbutton.image = photo
fontbutton.grid(row=0, column=5)





































mainloop()