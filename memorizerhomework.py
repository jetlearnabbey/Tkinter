from tkinter import *
from tkinter.filedialog import *


window = Tk()
window.title("Memorizer")
window.minsize(300, 400)
window.config(bg="pink")


top_frame = Frame(window, bg="pink")
top_frame.pack(pady=10)


open_btn = Button(top_frame, text="OPEN", fg="black", bg="lightgray", width=10, command=exit)
open_btn.grid(row=0, column=0, padx=5)


delete_btn = Button(top_frame, text="DELETE", fg="black", bg="lightgray", width=10, command=exit)
delete_btn.grid(row=0, column=1, padx=5)


save_btn = Button(top_frame, text="SAVE", fg="black", bg="lightgray", width=10, command=exit)
save_btn.grid(row=0, column=2, padx=5)


file_entry = Entry(window, font=("Arial", 12), width=25)
file_entry.pack(pady=10)


add_btn = Button(window, text="ADD", fg="black", bg="lightgray", width=10, command=exit)
add_btn.pack(pady=5)


frame = Frame(window, bg="pink")
frame.pack(pady=10)


listbox = Listbox(frame, width=35, height=10, bg="white", font=("Arial", 10))
listbox.grid(row=0, column=0)


scrollbar = Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)


for i in range(1, 99):
    listbox.insert(END, f"List {i}")


window.mainloop()
