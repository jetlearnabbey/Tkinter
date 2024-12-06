from tkinter import *
from tkinter.ttk import *


window=Tk()
window.title("Multiplication Generator")
window.config(bg="cyan")



title = Label(window,text="Mathematical Generator",font=("Arial",12))
title.grid(row=0,column=0,columnspan=3,pady=20)


picking = Label(window, text = "Number & Range: ",font=("Arial",12))
picking.grid(column=0,row=1,pady=4,padx=10)

#combobox creation
num = IntVar()
cobox = Combobox(window,textvariable=num,width=10)
cobox["values"]=tuple(range(1,101))

cobox.grid(row=1,column=1)
#radio buttons
num1 = IntVar()
rb1 = Radiobutton(window,text="10",variable=num1,value=10)
rb2 = Radiobutton(window,text="20",variable=num1,value=20)
rb3 = Radiobutton(window,text="30",variable=num1,value=30) 

rb1.grid(row=1,column=2)
rb2.grid(row=2,column=2,padx=20)
rb3.grid(row=3,column=2,padx=20)

def generate_button():
    tables = ""
    for i in range(num1.get()+1): 
        tables+=num.get()+"x"+str()

