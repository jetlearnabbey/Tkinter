import gtts
from tkinter import *
import os


root = Tk()
root.geometry("800x800")

def media():
  
  
    language = "es"
    gttsholder = gtts.gTTS(text=entry_box.get(),lang=language,slow=False,tld="es")
    gttsholder.save( "MyAudio.wav")
    os.system("MyAudio.wav")



frame1 =  Frame(root, bg="cyan",height="450")
frame1.pack(fill=X,pady=5,)

frame2 = Frame(root,bg="green",height="400")
frame2.pack(fill=X,pady=5)

entry_box = Entry(frame2,font=("Arial",20),width=35)
entry_box.pack(pady=100)

submit_button = Button(frame2,text="Submit!",font=("Arial",40),bg="yellow",fg="red",command=media)
submit_button.pack(pady=110)

title = Label(frame1,text="Text To Speech!",font=("Arial",40),bg="cyan")
title.pack(pady=75)

def media():
    language = "en"
    gttsholder = gtts.gTTS(text=entry_box.get(),lang=language,slow=False)
    gttsholder.save( "MyAudio.wav")
    os.system("MyAudio.wav")






mainloop()



