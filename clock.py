from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime

window = Tk()
window.title("CLOCK FOR GMT TIME")
now = datetime.datetime.now()
title2 = Label(window,text="My Digital Clock",font=("Arial",50))
title2.pack()


colors = ["red", "green", "yellow", "purple", "orange"]
color_index = 0  

def timer():
    global color_index
    string = strftime("%A/%d/%m")
    timelabel.config(text=string)
    
   
    current_color = colors[color_index]
    timelabel.config(background=current_color)
    daylabel.config(background=current_color)
    
   
    color_index = (color_index + 1) % len(colors)
    
    timelabel.after(1000, timer)

def day():
    string1 = strftime("%H:%M:%S %p")
    daylabel.config(text=string1)
    daylabel.after(1000, day)

timelabel = Label(window, font=("Times", 40, "bold"), background="red", foreground="blue")
timelabel.pack()
daylabel = Label(window, font=("Helvetica", 20, "bold"), background="red", foreground="blue")
daylabel.pack()

timer()
day()
mainloop()
