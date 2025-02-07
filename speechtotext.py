from tkinter import *
import speech_recognition as sr
import os
from tkinter import messagebox
from tkinter.filedialog import *

def translation():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recog.listen(source)
        try:
            text = recog.recognize_google(audio)
        except:
            text= "Sorry, could not recognise your voice."
        translator_teller.delete(1.0,END)
        translator_teller.insert(END,text)




def save_files():
    savefile = asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if savefile:
        text = translator_teller.get("1.0", END).strip()
        savefile.write(text)
        savefile.close()

root= Tk()
root.geometry("800x400")



title = Label(root,text="Speech to Text!",font=("Arial",40))
title.grid(row=0,column=1,padx=20,pady=20)


translator_btn = Button(root,text="Click on me.. to start recording!",command=translation)
translator_btn.grid(row=1,column=0,padx=20,pady=20)


save_btn = Button(root, text="Save Text",command=save_files)
save_btn.grid(row=1,column=2,pady=10,columnspan=3)

translator_teller = Text(root,width=60, height=10)
translator_teller.grid(row=1,column=1,padx=20,pady=20)





mainloop()