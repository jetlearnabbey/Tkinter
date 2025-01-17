from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox 
window = Tk()
window.config(bg="cyan")
#from tkinter.ttk import *

window.geometry("600x500")

address_book = {}

def cleartextboxes():
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    mobile_entry.delete(0,END)
    email_entry.delete(0,END)
    birthday_entry.delete(0,END)


def deletefile():
    selected = listbox.curselection()
    if selected:
        del address_book[listbox.get(selected)]
        listbox.delete(selected)
        cleartextboxes()
    else:
        messagebox.showerror(message="Please select a name to delete.")
def reset():
    cleartextboxes()
    listbox.delete(0,END)
    address_book.clear()
def openbutton():
    global address_book
    reset()
    openingfiles = askopenfile(title="Open")
    if openingfiles is not None:
        address_book = eval(openingfiles.read())
        for i in address_book.keys():
            listbox.insert(END,i)    
    else:
        messagebox.showerror(message="You haven't selected an address book.")

def savebutton():
    savefile = asksaveasfile(defaultextension=".txt")
    if savefile is not None:
      print(address_book,file=savefile)
      reset() 
    else:
        messagebox.showwarning(message="Your book has not been saved.")

def updatebutton():
    key = name_entry.get()
    if key == "":
        messagebox.showerror(message="The name cannot be empty.")
    else:
        if key not in address_book.keys():
            listbox.insert(END,key)
        address_book[key]=(address_entry.get(),birthday_entry.get(),mobile_entry.get(),email_entry.get())
        cleartextboxes()
    print(address_book)
def editbutton():
    selected = listbox.curselection()
    if selected:
        selected_name = listbox.get(selected)
        details = address_book.get(selected_name, ("", "", "", ""))
        name_entry.delete(0, END)
        name_entry.insert(0, selected_name)
        address_entry.delete(0, END)
        address_entry.insert(0, details[0])
        birthday_entry.delete(0, END)
        birthday_entry.insert(0, details[1])
        mobile_entry.delete(0, END)
        mobile_entry.insert(0, details[2])
        email_entry.delete(0, END)
        email_entry.insert(0, details[3])
    else:
        messagebox.showerror(message="Please select a name to edit.")






def display(event):
    root = Toplevel(window)
    infoselection = listbox.curselection()
    contents =  ""
    if infoselection:
        key = listbox.get(infoselection)
        details = address_book[key]

        contents = "Name:"+ key+"\n"
        contents+="Address: "+details[0]+"\n"
        contents+="Mobile: "+details[1]+"\n"
        contents+="Email: "+details[2]+"\n"
        contents+="Birthday: "+details[3]+"\n"

    toplevelabel = Label(root,text=contents)
    toplevelabel.place(x=40,y=60)












































































































































        






         


    

        






open_btn = Button(window,text="Open",bg="red",fg="lightgray",font=("Arial",15),command=openbutton)
open_btn.place(x=300,y=4)

title = Label(window,text="My Address Book",font=("Arial",20))
title.place(x=50,y=4)

listbox = Listbox(window,height = 20, width=30,font = ("Arial",10))
listbox.place(x=20,y=60)
listbox.bind("<<ListboxSelect>>",display)

name_entry = Entry(window,width=10,font=("Arial",20))
name_entry.place(x=410,y=55)

name_label = Label(window,text="Name: ",font=("Arial",20))
name_label.place(x=300,y=55)

address_label=  Label(window, text = "Address: ",font=("Arial",20))
address_label.place(x=270, y=106)


address_entry = Entry(window, width=10,font=("Arial",20))
address_entry.place(x=410,y=106)

mobile_label = Label(window,text="Mobile: ",font=("Arial",20))
mobile_label.place(x=289,y=150)

mobile_entry = Entry(window,width=10,font=("Arial",20))
mobile_entry.place(x=415,y=150)

email_label = Label(window,text="Email: ",font=("Arial",20))
email_label.place(x=307,y=194)

email_entry = Entry(window,width=10,font=("Arial",20))
email_entry.place(x=420,y=194)

birthday_label = Label(window,text="Birthday: ",font=("Arial",20))
birthday_label.place(x=285,y=258)

birthday_entry = Entry(window,width=10,font=("Arial",20))
birthday_entry.place(x=415,y=253)

update_addbtn = Button(window,text="Update/Add",fg="red",bg="lightgray",font=("Arial",15),command=updatebutton)
update_addbtn.place(x=415,y=310)

save_btn = Button(window,text="Save",fg="red",bg="lightgray",width=20,font=("Arial",15),command=savebutton)
save_btn.place(x=330,y=440)

delete_btn = Button(window,text="Delete",fg="red",bg="lightgray",font=("Arial",15),command=deletefile)
delete_btn.place(x=140,y=420)

edit_btn  = Button(window,text="Edit",fg="red",bg="lightgray",font=("Arial",15),command=editbutton)
edit_btn.place(x=40,y=420)

mainloop()
