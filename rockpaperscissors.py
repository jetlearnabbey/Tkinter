from tkinter import *
import tkinter.font as font
import random

computerpoints = 0
playerpoints = 0

options = [("Rock",0),("Paper",1),("Scissors",2)]
def tie():
    global playerpoints,computerpoints
    result_label.config(text="It is a TIE!")
    yourscore.config(text="Player Score: "+str(playerpoints))
    computerscore.config(text = "Computer Score: "+str(computerpoints))

def computerwins():
    global playerpoints,computerpoints
    computerpoints+=1
    result_label.config(text="The computer has won.")
    yourscore.config(text="Player Score: "+str(playerpoints))
    computerscore.config(text = "Computer Score: "+str(computerpoints))

def playerwins():
    global playerpoints,computerpoints
    playerpoints+=1
    result_label.config(text="The player has won.")
    yourscore.config(text="Player Score: "+str(playerpoints))
    computerscore.config(text = "Computer Score: "+str(computerpoints))

def playerchoice(playerinput):
    computerchoice1  = random.choice(options)
    print(computerchoice1)
    selection.config(text = "You Selected: "+playerinput[0])
    computerchoice.config(text = "Computer Selected: "+computerchoice1[0])
    if computerchoice1==playerinput:
        tie()
    if playerinput[1] == 0:
        if computerchoice1[1] == 1:
            computerwins()
        if computerchoice1[1] == 2:
            playerwins()

    elif playerinput[1] == 1:
        if computerchoice1[1] == 0:
            playerwins()
        if computerchoice1[1] == 2:
            computerwins()

    elif playerinput[1] == 2:
        if computerchoice1[1] == 1:
            playerwins()
        if computerchoice1 [1] == 0:
            computerwins()




  

  

window = Tk()
window.title("Rock, Paper, Scissors!")
title = Label(window, text="Rock, Paper, Scissors!", font=font.Font(size=20), fg="blue")
startingtitle = Label(window, text="Start the Game!", font=font.Font(size=15), fg="green", pady=8)
title.pack()
startingtitle.pack()


f1 = Frame(window)
f1.pack()


youroptions = Label(f1, text="Your Options:", font=font.Font(size=12), fg="purple")
youroptions.grid(row=0, column=0, columnspan=3, pady=8)

selection = Label(f1, text="You Selected: ---", font=font.Font(size=10), fg="purple")
selection.grid(row=4, column=0, pady=8, columnspan=3,)

computerchoice = Label(f1, text="Computer Selected: ---", font=font.Font(size=10), fg="purple")
computerchoice.grid(row=4, column=0, pady=8)

yourscore = Label(f1, text="Your Score: 0", font=font.Font(size=10), fg="purple")
yourscore.grid(row=8, column=0, pady=8 )

computerscore = Label(f1, text="Computer Score: 0", font=font.Font(size=10), fg="purple")
computerscore.grid(row=7, column=0, pady=4)

result_label = Label(f1, text="Let's Start The Game!", font=font.Font(size=12), fg="red")
result_label.grid(row=6, column=0, pady=8)


rockbutton = Button(f1, text="Rock", bg="orange", width=15, command=lambda: playerchoice(options[0]))
rockbutton.grid(row=1, column=0, padx=8, pady=5)

paperbutton = Button(f1, text="Paper", bg="pink", width=15, command=lambda: playerchoice(options[1]))
paperbutton.grid(row=1, column=1, padx=8, pady=5)

scissorsbutton = Button(f1, text="Scissors", bg="green", width=15, command=lambda: playerchoice(options[2]))
scissorsbutton.grid(row=1, column=2, padx=8, pady=5)



mainloop()
