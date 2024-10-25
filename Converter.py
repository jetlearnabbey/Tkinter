from tkinter import *

def convert_weight():
    
        gram =  float(entry_weight.get())*1000
    
        pounds = float(entry_weight.get())*2.20462
        ounce = float(entry_weight.get())*35.274
        gramentry.delete("1.0",END)
        gramentry.insert(END,gram)
        poundentry.delete("1.0",END)
        poundentry.insert(END,pounds)
        ounceentry.delete("1.0",END)
        ounceentry.insert(END,ounce)
       






window = Tk()
window.title("Weight Converter")
window.geometry("500x150")
window.config(bg="red")


entererlabel = Label(window, text="Enter weight in Kg", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entry_weight = Entry(window, font=("Arial", 12), width=10)
entry_weight.grid(row=0, column=1, padx=5, pady=5)


converterbutton = Button(window, text="Convert", font=("Arial", 12), command=convert_weight).grid(row=0, column=2, padx=10, pady=5, ipadx=10)


gramslabel = Label(window, text="Grams", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
poundslabel = Label(window, text="Pounds", font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
ouncelabel = Label(window, text="Ounces", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady = 5)


gramentry = Text(window, font=("Arial", 12,"bold"), width=10,height=1)
gramentry.grid(row=2, column=0, padx=5, pady=5, ipadx=5)

poundentry = Text(window, font=("Arial", 12,"bold"), width=10,height=1)
poundentry.grid(row=53, column=1, padx=5, pady=5, ipadx=5)

ounceentry = Text(window, font=("Arial", 12,"bold"), width=10,height=1)
ounceentry.grid(row=2, column=2, padx=5, pady=5, ipadx=5)






mainloop()
