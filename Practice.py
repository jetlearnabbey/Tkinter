from tkinter import * 
from tkinter.filedialog import *


window = Tk()
window.config(bg="blue")
window.minsize("500x500"




def openfile():
opening = askopenfile(title = "Open File")
if opening is not None:
listbox.delete(0,END)
