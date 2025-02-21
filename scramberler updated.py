
from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.config(bg="black")
window.geometry("800x800")

words = ["london", "evening", "happy", "coding", "home", "egg", "table", "games", "hyper", "realistic", "computer", "cat", "sad", "omnipotent", "arms"]

scrambled_words = []



for i in range(len(words)):
    scrambled_word = "".join(random.sample(words[i], len(words[i])))
    scrambled_words.append(scrambled_word)
print(scrambled_word)

num = random.randrange(0,len(words))

def reset():
  global num
  num = random.randrange(0,len(words))
  scrambledword.config(text=scrambled_words[num])
  entry_box.delete(0,END)

score = 0
qno = 0
def check():
    global score,qno,num
    qno+=1
    storer = entry_box.get()

 
    if storer == words[num]:

        
      score+=1
      messagebox.showinfo(message="Congratulations, correct answer!")

    else:
      messagebox.showerror(message="Sorry, incorrect answer.")
    scorecounter = "Score: "+str(score)+"/"+str(qno)
    scorecount.config(text=scorecounter)

    reset()
      
      

      
   


title = Label(window, text="JUMBLED WORD GAME", bg="black", fg="white", font=("Arial", 30))
title.pack(pady=5)

scorecount = Label(window, text="Score: ", bg="black", fg="white", font=("Arial", 20))
scorecount.pack(pady=20)

entry_box = Entry(window, font=("Arial", 20), width=20)
entry_box.pack(pady=25)

scrambledword = Label(window, bg="blue", fg="white",font=("Arial", 20),text=scrambled_words[num])
scrambledword.pack(pady=30)

check_button = Button(window, text="Check", fg="green", bg="lightgray", font=("Arial", 20), command=check)
check_button.pack(pady=35)

reset_button = Button(window, text="Reset", fg="yellow", bg="lightgray", font=("Arial", 20), command=reset)
reset_button.pack(pady=40)



mainloop()
