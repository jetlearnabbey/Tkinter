from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox


window=Tk()
window.title("Pizza App")
window.config(bg="pink")



title = Label(window,text="Welcome to Pizza Hut",font=("Arial",12))
title.grid(row=0,column=0,columnspan=3,pady=20)

quantitychoice = Label(window,text="Select Quantity: ",font=("Arial",12))
quantitychoice.grid(column=0,row=3)

picking = Label(window, text = "Select Your Fav Pizza: ",font=("Arial",12))
picking.grid(column=0,row=1,pady=4,padx=10)

#combobox creation
options = StringVar()
quantity = IntVar()
cobox = Combobox(window,textvariable=options,width=10)
cobox["values"]=("Cheeseness",
"Pepperoni PE",
"Veggie Super",
"BBQ Chicken ",
"Margherita Joy")
cobo =Combobox(window,textvariable=quantity,width=10)

cobo["values"]=tuple(range(1,11))




cobox.grid(row=1,column=1)
cobo.grid(row=3,column=1)


rb1 = Radiobutton(window,text="S",value=20)
rb2 = Radiobutton(window,text="M",value=40)
rb3 = Radiobutton(window,text="L",value=60) 

rb1.grid(row=1,column=2)
rb2.grid(row=2,column=2,padx=20)
rb3.grid(row=3,column=2,padx=20)



    


def order_placement():
    tkinter.messagebox.showinfo(message="You ordered: ")

def price_info():
    tkinter.messagebox.showinfo(message="A small is £20, a medium one is £40 and a large is £60.")
    






order=Button(window,text="Order",command=order_placement)
order.grid(row=0,column=2)

prices=Button(window,text="Prices",command=price_info)
prices.grid(row=0,column=6)


table = Label(window)
table.grid(row=1,column=6)


mainloop()
