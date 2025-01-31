from tkinter import *
import speech_recognition as sr
import os
from tkinter import messagebox
from tkinter.filedialog import *


root= Tk()
root.geometry("800x400")



title = Label(root,text="Speech to Text!",font=("Arial",40))
title.grid(row=0,column=1,padx=20,pady=20)


translator_btn = Button(root,text="Click on me.. to start recording!",command=None)
translator_btn.grid(row=1,column=0,padx=20,pady=20)


save_btn = Button(root, text="Save Text",command=None)
save_btn.grid(row=1,column=2,pady=10,columnspan=3)

translator_teller = Text(root,width=60, height=10)
translator_teller.grid(row=1,column=1,padx=20,pady=20)



mainloop()
