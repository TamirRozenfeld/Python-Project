from tkinter import *
# Tkinter is the de facto way in Python to create Graphical User interfaces

from tkinter.ttk import *
# ttk is module that is used to style the tkinter widgets.

from time import strftime
# strftim is used to convert date and time objects to their string representation


root = Tk()
root.title("Tamir_Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
# 1000 is one second, on every one second we call the time function

#                          "style"    "size"
label = Label(root, font=("ds-digital", 80),background = "black", foreground = "cyan")
# Tkinter Label is a widget that is used to implement display boxes where you can place text or images
label.pack(anchor='center')
# Anchors are used to define where text is positioned relative to a reference point.
time()
# call the function time

mainloop()
# This method will loop forever, waiting for events from the user, until the user exits the program. 