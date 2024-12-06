from tkinter import *
from tkinter import messagebox
import time


window = Tk()
window.title("Countdown")
window.geometry("300x300")
window.config(bg="blue")

hour =   StringVar()
minute = StringVar()
second=  StringVar()
hour.set("00")
minute.set("00")
second.set("00")


    

def finish_message():
    messagebox.showinfo(message="Succesfully registered!")


def registering():


    signinwindow = Toplevel(window)
    username = Label(signinwindow,text="Username",font=("Arial",20,"bold"))
    username.place(x=50,y=100)
    usernameentry = Entry(signinwindow,width=20)
    usernameentry.place(x=200,y=110)
    password = Label(signinwindow,text="Password",font=("Arial",20,"bold"))
    password.place(x=50,y=150)
    passwordentry = Entry(signinwindow,width=20,show="*")
    passwordentry.place(x=200,y=160)
    finish = Button(signinwindow,text="Register",fg="white",bg="cyan",font=("Arial",20,"bold"),command=finish_message)
    finish.place(x=200,y=210)






hr= Entry(window,textvariable=hour,width=5,font=("Arial",20,"bold"))
hr.place(x=20,y=100)

min = Entry(window,textvariable=minute,width=5,font=("Arial",20,"bold"))
min.place(x=110,y=100)

sec = Entry(window,textvariable=second,width=5,font=("Arial",20,"bold"))
sec.place(x=210,y=100)

seclabel = Label(window,text="Seconds",font=("Arial",15,"bold"))
seclabel.place(x=210,y=50)

minlabel = Label(window,text="Minutes",font=("Arial",15,"bold"))
minlabel.place(x=110,y=50)

hrlabel = Label(window,text="Hours",font=("Arial",15,"bold"))
hrlabel.place(x=20,y=50)







accountbar = Menu(window)
account = Menu(accountbar,tearoff=0)
accountbar.add_cascade(label="My Account",menu=account)
account.add_command(label="Register",command=registering)
window.config(menu=accountbar)
def countdown():

  temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
   
    
  while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins >= 60:
            hours, mins = divmod(mins, 60)
        
        # Update the displayed time
        hour.set(f"{hours:02d}")
        minute.set(f"{mins:02d}")
        second.set(f"{secs:02d}")

        begincountdown.config(state="disabled")
        window.update()
        time.sleep(1)
        
     
        if temp == 10:
            messagebox.showinfo(message="Warning, 10 seconds left!")
        
        
        if temp == 0:
            messagebox.showinfo(message="Time is up!")
            begincountdown.config(state="normal")

        
        temp -= 1  

def new_window():
    signinwindow = Toplevel(window)
    signinwindow.config(bg="blue")
    signinwindow.title("Registering")
    
     





    

begincountdown = Button(window,text="Begin Countdown!",font=("Arial",15,"bold"),foreground="cyan",background="red",command=countdown)
begincountdown.place(x=20,y=150)






mainloop()

