# import everthing from the tikinter module

from tkinter import *

#create a tkinter window
window = Tk()
window.title("Window Title")
# using geometry method to find dimensions
window.geometry("400x400")
window.config(background="blue")
#label for username
username = Label(window,text="Username").place(x=50,y=100)
password = Label(window,text="Password").place(x=50,y=140)
userinput = Entry(window,width=30).place(x=150,y=100)
userinput2 = Entry(window,show="*",width=30).place(x=150,y=140)
# creating a button
button = Button(window,text = "Click Me!",bd="5",background = "red",command=window.destroy).place(x=160,y=200)
#setting the position of the button using pack method
#button.pack(side="top")
#button.grid(row=1,column=2)












window.mainloop()
