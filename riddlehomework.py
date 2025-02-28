from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(bg="cyan")
window.geometry("400x200")  


riddles = [
    "The more you take, the more you leave behind. What am I?",
    "I have keys but open no locks. What am I?",
    "What has to be broken before you can use it?",
    "I speak without a mouth and hear without ears. What am I?",
    "The more you remove from me, the bigger I get. What am I?",
    "What has one eye but cant see?"
]

correct_answers = ["footsteps", "piano", "egg", "echo", "hole", "needle"]

answered_riddle = 0

def check_answer():
    global answered_riddle
    user_answer = answer_entry.get() 
    correct_answer = correct_answers[answered_riddle]

    if user_answer == correct_answer:
        messagebox.showinfo(message="Correct! You got it right!")
    else:
        messagebox.showinfo(message ="Wrong. You got in incorrect.")

    answered_riddle += 1

    if answered_riddle < len(riddles):
        riddle_label.config(text=riddles[answered_riddle])
        answer_entry.delete(0, END)
    else:
        riddle_label.config(text="You completed all the riddles! Get ready for Level 2!")
        answer_entry.config(state=DISABLED)
        submit_button.config(state=DISABLED)
        lvl2 = Button(window,text="Press this to go to Level 2!",font=("Arial",10),command=level2)
        lvl2.pack(pady=10)


def level2():
    answer_entry.config(state=NORMAL)
    submit_button.config(state=NORMAL)




riddle_label = Label(window, text=riddles[answered_riddle], font=("Arial", 14), wraplength=380, bg="cyan")
riddle_label.pack(pady=10)

answer_entry = Entry(window, font=("Arial", 12))
answer_entry.pack(pady=5)

submit_button = Button(window, text="Submit", bg="red",font=("Helvetica",10),command=check_answer) 
submit_button.pack(pady=5)

mainloop()
