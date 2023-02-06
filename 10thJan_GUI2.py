#!/usr/bin/python3

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup',message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button1 = Button(window, text='click', command=reply)
button.pack()
button1.pack()
window.geometry("500x200")
window.mainloop()
