# import everthing from the tikinter module

from tkinter import *

#create a tkinter window
window = Tk()
window.title("My Homework")
# using geometry method to find dimensions
window.geometry("500x500")
window.config(background="purple")
#label for username
username = Label(window,text="Username",font = ("Arial",10,"bold") ).place(x=50,y=100)
password = Label(window,text="Password",font = ("Arial",10,"bold")).place(x=50,y=140)
dob = Label(window,text="Date of Birth",font = ("Arial",10,"bold")).place(x=50,y=180)
userinput = Entry(window,width=30,font = ("Arial",10,"underline")).place(x=150,y=100)
userinput2 = Entry(window,show="*",width=30).place(x=150,y=140)
userinput3 = Entry(window,width=30,font = ("Arial",10,"underline")).place(x=150,y=180)
# creating a button
button = Button(window,text = "Click Here!",bd="10",activebackground = "green",activeforeground = "blue" ,command=window.destroy,font=("Arial",16,"italic")).place(x=160,y=230)
#setting the position of the button using pack method
#button.pack(side="top")
#button.grid(row=1,column=2)












window.mainloop()
