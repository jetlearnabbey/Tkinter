from tkinter import *
import random
import tkinter.messagebox

window = Tk()
window.title("Guessing Game")
window.minsize(950,350)
window.config(bg="blue")

def buttonok():
    name = nameentry.get()
    tkinter.messagebox.showinfo(message="Well," +name+ " my number is between 1 and 5.")


secretnum = random.randint(1,5)

def secretnumber():
    guessentryinput = int(guessentry.get())
    if guessentryinput>secretnum:
        tkinter.messagebox.showinfo(message="The guess is greater.")
    elif guessentryinput<secretnum:
        tkinter.messagebox.showinfo(message="The guess is lower.")
    else:
        tkinter.messagebox.showinfo(message="You got it right.")

title = Label(window,text="Welcome to the Game!",font=("Arial",40))
title.pack()

namequestion = Label(window,text="What is your name?",font=("Arial",20))
namequestion.place(x=20,y=100)

nameentry = Entry(window,font=("Arial",30,"bold"),width=10)
nameentry.place(x=350,y=100)

okbutton = Button(window,text="OK",font=("Arial",21),command=buttonok)
okbutton.place(x=700,y=100)

namequestion = Label(window,text="Take a guess!",font=("Arial",20))
namequestion.place(x=20,y=200)

guessentry = Entry(window,font=("Arial",30,"bold"),width=10)
guessentry.place(x=350,y=200)

guessbutton = Button(window,text="Guess",font=("Arial",21),command=secretnumber)
guessbutton.place(x=700,y=200)













