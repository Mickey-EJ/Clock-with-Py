from tkinter import *
from tkinter.ttk import *

from time import strftime

# UI for clock
root = Tk()
root.title("Clock")

def time():
    #12 hour time format
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#clock face
label = Label(root, font=("ds_digital", 80), background = "black", foreground = "cyan")
label.pack(anchor = 'center')
time()

mainloop()