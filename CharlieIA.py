from email.mime import image
from tkinter import *
# from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import _Anchor
from turtle import width
from webbrowser import BackgroundBrowser
from Face_detector import *
from tkinter.filedialog import *

# import time
# import datetime
# import os
# import sys


    #initialisation of the screen
root = Tk()
# root.attributes("-fullscreen", False)
root.config(background='#ADD8E6')
# root.bind("x", quit)

    #defining font-style and size
fnt = font.Font(family="Rockwell", size = 30, weight = "bold")
txt = StringVar()

    #creating a label widget
lbl = Label(root, text= "WALDO IA", font=fnt, foreground="white", background= '#ADD8E6', border=1, relief=SUNKEN )
lbl.place(relx = 0.5, rely = 0.5, anchor = "center")


    #create an image
width = 100
height = 100
image = PhotoImage(file = "images/conan.png").zoom(35).subsample(32)
canvas = Canvas(root, width=width, height=height, bg= '#ADD8E6')
canvas.create_image(width/2, height/2, image = image)

def ajoutVid():
    filepath =askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png'),('all files','.*')])
    photo = PhotoImage(file=filepath)
    canvas2 = Canvas(root, width=photo.width(), height=photo.height(), bg='#ADD8E6')
    canvas2.create_image(0, 0, anchor=NW, image=photo)
    canvas2.pack()

b = Button(root,command= ajoutVid, text="Ajout vidéo", activeforeground="black", activebackground="deepskyblue", pady=10, background= "white")
b2 = Button(root, text="Analyse", activeforeground="black", activebackground="deepskyblue", pady=10, background= "white")
b3 = Button(root, text="Illisible", activeforeground="black", activebackground="deepskyblue", pady=10, background= "white")



    #shoving it onto the screen
lbl.pack()
canvas.pack()
b.pack(side= BOTTOM)
b2.pack(side= BOTTOM)
b3.pack(side= BOTTOM)

root.mainloop()

# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', ':0.0')


# #create main window
# master = Tk()
# master.title("tester")
# master.geometry("300x100")


# #make a label for the window
# myLabel = Tk.Label(master, text='Où est Charlie ?')
# # Lay out label
# myLabel.pack()

# # Run forever!
# master.mainloop()
