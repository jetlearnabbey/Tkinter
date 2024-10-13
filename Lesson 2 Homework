# import everything from the tkinter module
from tkinter import *
from tkinter.ttk import *



window = Tk()


#create a tkinter window
window = Tk()
window.title("My Homework")
# using geometry method to find dimensions
window.geometry("810x810")
window.config(background="blue")
username = Label(window,text="Email",font = ("Arial",10,"bold") ).place(x=50,y=100)
username = Label(window,width=80,text="Teacher Application",font = ("Arial",30,"bold") ).place(x=50,y=45)
password = Label(window,text="Password",font = ("Arial",10,"bold")).place(x=50,y=140)
dob = Label(window,text="Date of Birth",font = ("Arial",10,"bold")).place(x=50,y=180)
userinput = Entry(window,width=30,text = "@gmail.com",font = ("Arial",10)).place(x=150,y=100)
userinput2 = Entry(window,show="*",width=30).place(x=150,y=140)
userinput3 = Entry(window,width=30,font = ("Arial",10)).place(x=150,y=180)
# creating a button

userinput4 = Entry(window,width=30,font = ("Arial",10)).place(x=150,y=280)
question1 = Label(window,text="Where were you born?",font = ("Arial",10,"bold") ).place(x=155,y=250)
userinput5 = Entry(window,width=30,font = ("Arial",10)).place(x=150,y=350)
question2 =  Label(window,text="Previous Occupation?",font = ("Arial",10,"bold") ).place(x=155,y=320)
userinput6 = Entry(window,width=70,font = ("Arial",10)).place(x=150,y=410)
question3 = Label(window,text="Reason for leaving current job?",font = ("Arial",10,"bold") ).place(x=155,y=380)
progress = Progressbar(window,orient=HORIZONTAL,length=200,mode='determinate')
window.title("QuickHire")

#creating menu bar
menubar = Menu(window)
#adding the file commands
jobcareers = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Job Careers",menu=jobcareers)
jobcareers.add_command(label="Job Spaces",command=None)
jobcareers.add_command(label="Locations",command=None)
jobcareers.add_command(label="Job FAQ",command=None)
jobcareers.add_separator()
jobcareers.add_command(label="Exit",command=None)
#adding options
aboutus = Menu(menubar,tearoff=0)
menubar.add_cascade(label="About Us",menu=aboutus)
aboutus.add_command(label="Company History",command=None)
aboutus.add_command(label="Awards",command=None)
aboutus.add_command(label="Meet The Team",command=None)
aboutus.add_command(label="Goals",command=None)
aboutus.add_command(label="Testimonials",command=None)
aboutus.add_separator()

support = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Contact/Support",menu=support)
support.add_command(label="Help",command=None)
support.add_command(label="Number",command=None)
support.add_command(label="Report Issue",command=None)
support.add_separator()

ratings = Menu(menubar,tearoff=1)
menubar.add_cascade(label="Ratings",menu=ratings)
ratings.add_command(label="Trustpilot",command=None)
ratings.add_command(label="Comments",command=None)
ratings.add_separator()



window.config(menu=menubar)

    
   
#making progress bar
def loading():
    import time
    progress["value"]=25
    window.update_idletasks()
    time.sleep(1)

    progress["value"]=46
    window.update_idletasks()
    time.sleep(1)

    progress["value"]=69
    window.update_idletasks()
    time.sleep(1)
    
    progress["value"]=70
    window.update_idletasks()
    time.sleep(1)
    
    progress["value"]=79
    window.update_idletasks()
    time.sleep(1)
    

    progress["value"]=100
    window.update_idletasks()
    time.sleep(1)
     
progress.pack()




 
Button(window,text="Submit Application",command=loading).pack()











window.mainloop()
