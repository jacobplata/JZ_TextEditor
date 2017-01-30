from Tkinter import *
from PIL import Image, ImageTk
import Tkinter as tk
import tkFont


def nothing():
    print "a"

def r():
    print "r"

def save():
    f = open('Readme.txt', 'w')
    t = text1.get(1.0,END)
    f.write(t)
    f.close()

def openfile():
    f = open('Readme.txt', 'r')
    text1.insert(END, f.read())
    f.close()

def justcenter():
    deletealltags()
    text1.tag_configure("center", justify='center')
    text1.tag_add("center", 1.0, "end")
    
def justleft():
    deletealltags()
    text1.tag_configure("left", justify='left')
    text1.tag_add("left", 1.0, "end")
    
def justright():
    deletealltags()
    text1.tag_configure("right", justify='right')
    text1.tag_add("right", 1.0, "end")

def makeitalic():
    deletealltags()
    text1.tag_configure("italic", font = ('Sans','10','italic'))
    text1.tag_add("italic", 1.0, "end")

    
def makebold():
    deletealltags()
    text1.tag_configure("bold", font = ('Sans','10','bold'))
    text1.tag_add("bold", 1.0, "end")
    
def makeunderline():
    deletealltags()
    text1.tag_configure("underline", font = ('Sans','10','underline'))
    text1.tag_add("underline", 1.0, "end")

def deletealltags():
    text1.tag_delete("underline", 1.0, "end")
    text1.tag_delete("bold", 1.0, "end")
    text1.tag_delete("italic", 1.0, "end")
    text1.tag_delete("right", 1.0, "end")
    text1.tag_delete("left", 1.0, "end")
    text1.tag_delete("center", 1.0, "end")
    
    
root = Tk()
root.title("Low Key Text Editor")


#File Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Save", command=save)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#Zoom Menu
zoommenu = Menu(menubar, tearoff=0)
zoommenu.add_command(label="100%", command=nothing)
zoommenu.add_command(label="200%", command=nothing)
zoommenu.add_command(label="50%", command=nothing)

menubar.add_cascade(label="Zoom", menu=zoommenu)
root.config(menu=menubar)

#Buttons
image = Image.open("bold.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

boldbutton = Button(root, text="B", image=photo, command=makebold)
boldbutton.image = photo # keep a reference!
boldbutton.grid(row=0, column=0, sticky=EW)

image = Image.open("italic.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

italicbutton = Button(root, text="I", image=photo, command=makeitalic)
italicbutton.image = photo
italicbutton.grid(row=0, column=1, sticky=EW)

image = Image.open("underline.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

underlinebutton = Button(root, text="U", image=photo, command=makeunderline)
underlinebutton.image = photo
underlinebutton.grid(row=0, column=2, sticky=EW)

image = Image.open("left.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

leftbutton = Button(root, text="U", image=photo, command=justleft)
leftbutton.image = photo
leftbutton.grid(row=0, column=3, sticky=EW)

image = Image.open("center.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

centerbutton = Button(root, text="U", image=photo, command=justcenter)
centerbutton.image = photo
centerbutton.grid(row=0, column=4, sticky=EW)

image = Image.open("right.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

rightbutton = Button(root, text="U", image=photo, command=justright)
rightbutton.image = photo
rightbutton.grid(row=0, column=5, sticky=EW)

image = Image.open("font.png")
image = image.resize((25,25,))
photo = ImageTk.PhotoImage(image)

fontbutton = Button(root, text="U", image=photo, command=nothing)
fontbutton.image = photo
fontbutton.grid(row=0, column=6, sticky=EW)


#Text)
text1 = Text(root, height=50, width=100)
text1.grid(row=1, column=0, rowspan=10, columnspan=10, sticky=EW)








mainloop()