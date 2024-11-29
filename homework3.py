from tkinter import *
import random
import tkinter.messagebox


window = Tk()
window.title("Guessing Game")
window.minsize(950,550)
window.config(bg="blue")


def story():
    tkinter.messagebox.showinfo(message="Manchester Charity is dedicated to supporting homeless individuals and families in the city. They provide food, shelter, and resources to help people get back on their feet. Through community donations and volunteer work, they make a real difference in improving lives.")


def pay():
  tkinter.messagebox.showinfo(message="If you want to pay with card, you must open an account so we can take £500 a month, but if you pay with cash, you must come to our shop to pay us the £500 in-person.")
   


def buttonok():
    name = nameentry.get()

    if name=="":
     tkinter.messagebox.showerror(message = "Please enter a valid name.")
    else:
        tkinter.messagebox.showinfo(message="Now, "+name+ " ,you have to enter in your age.")

  


    


def normal():
    tkinter.messagebox.showwarning(message="For bonus questions, you must pay our monthly subscription of £500. Click on Payment and you will have to enter in your card details.")
    

 
       
  

paybar = Menu(window)
payment = Menu(paybar,tearoff=0)
paybar.add_cascade(label="Payment",menu=payment)
payment.add_command(label="Card Details",command=pay)
payment.add_command(label="Manchester Charity",command=story)



    




window.config(menu=paybar)

secretnum = 5

secretnum1 = random.randint(1,5)


product = secretnum*secretnum1 

def secretnumber():
    guessentryinput = int(guessentry.get())
    name = nameentry.get()
    if guessentryinput>product:
     tkinter.messagebox.showinfo(message=  "Now, "+name+ " your guess is greater than the answer.")
    elif guessentryinput<product:
        tkinter.messagebox.showinfo(message="Now, "+name+ " ,your guess is lower than the answer.")



    
    if guessentryinput==product:
        tkinter.messagebox.showinfo(message="You got it right!")
        

def submit():
    ageentryfield = (ageentry.get())
    

    if ageentryfield == "":
        tkinter.messagebox.showerror(message= "Please enter a valid age. ")

    else:
        tkinter.messagebox.showinfo(message= "Your age has been submitted. You are "+ageentryfield+" years old. Now you must guess a number multiplied by 5.")

   

product1 = 52
product2 = 53

def realanswer():
    answerinput = int(extraentry.get())
    if answerinput == product2:
        tkinter.messagebox.showinfo(message="The answer you put, 53, is correct! Great job!")
        exit()
    elif answerinput == product1:
        tkinter.messagebox.showinfo(message="So close!")
    else:
            tkinter.messagebox.showinfo(message="The answer you put is incorrect. Remember, BIDMAS!")





    
title = Label(window,text="Maths Multiplication Quiz!",font=("Arial",40))
title.pack()

namequestion = Label(window,text="What is your name?",font=("Arial",20))
namequestion.place(x=20,y=100)

nameentry = Entry(window,font=("Times",30,"bold"),width=10)
nameentry.place(x=350,y=100)

okbutton = Button(window,text="OK",font=("Arial",21),foreground="purple",background="cyan",command=buttonok)
okbutton.place(x=700,y=100)

guessquestion = Label(window,text="Take a guess!",font=("Arial",20))
guessquestion.place(x=20,y=300)

guessentry = Entry(window,font=("Times",30,"bold"),width=10)
guessentry.place(x=350,y=300)

guessbutton = Button(window,text="Guess",font=("Arial",21),foreground="purple",background="cyan",command=secretnumber)
guessbutton.place(x=700,y=300)

normalbutton = Button(window,text="Bonus Question",font=("Arial",21),foreground="purple",background="cyan",command=normal)
normalbutton.place(x=650,y=550)

agequestion = Label(window,text="What is your age?",font=("Arial",20))
agequestion.place(x=20,y=200)

submitbutton = Button(window,text="Submit",font=("Arial",21),foreground="purple",background="cyan",command=submit)
submitbutton.place(x=700,y=200)

ageentry = Entry(window,font=("Times",30,"bold"),width=10)
ageentry.place(x=350,y=200)

extraquestion = Label(window,text="What is 21+69x2/3?",font=("Arial",20))
extraquestion.place(x=20,y=400)

answerbutton = Button(window,text="Answer",font=("Arial",21),foreground="purple",background="cyan",command=realanswer)
answerbutton.place(x=700,y=400)





extraentry = Entry(window,font=("Times",30,"bold"),width=10)
extraentry.place(x=350,y=400)


mainloop()
















