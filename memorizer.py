from tkinter import *
from tkinter.filedialog import *


window = Tk()
window.minsize(200,300)
window.config(bg="blue")

def open_files():
  openfile = askopenfile(title="Open")
  if openfile is not None:
     listbox.delete(0,END)
     readfile = openfile.readlines()
     for i in readfile: 
      listbox.insert(END,i)
def save_files():
   savefile = asksaveasfile(defaultextension = ".txt")
   if savefile is not None:
      for i in listbox.get(0,END):
         print(i,file=savefile)
      listbox.delete(0,END)
def add_files():
   listbox.insert(END,fileentry.get())
   fileentry.delete(0,END)
def delete_files():
   selection = listbox.curselection()
   if selection:
      listbox.delete(selection)
     


save = Button(window,text="Save",fg="cyan",bg="green",command=save_files)
save.pack(pady=10)

fileentry = Entry(window,font=("Arial",12,"bold"),width=20)
fileentry.pack(pady=10)

add = Button(window,text="Add",fg="cyan",bg="red",command=add_files)
add.pack(pady=5)

frame = Frame(window)
frame.pack(pady=20)

open = Button(frame,text="Open",fg="cyan",bg="purple",command=open_files)
open.grid(row=0,column=0)


scrollbar = Scrollbar(frame,orient="vertical")
scrollbar.grid(row=0,column=3)

listbox = Listbox(frame,width=70,yscrollcommand=scrollbar.set)

for i in range(1,100):
    listbox.insert(END,"List"+ str(i))
listbox.grid(row=0,column=2)
scrollbar.config(command=listbox.yview)

delete = Button(frame,text="Delete",fg="cyan",bg="pink",command=delete_files)
delete.grid(row=0,column=1)







