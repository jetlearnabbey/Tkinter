from tkinter import *
import calendar
def showcal():
    win = Tk()
    win.config(background="white")
    win.title("CALENDAR")
    win.geometry("550x600")
    #get method to return the contents of a field
    cal_year = int(entryear.get())
    cal_content = calendar.calendar(cal_year)
    #creating text widget for displaying the calendar
    text_cal = Text(win,font="Consolas 10",height = 60, width=80)

    text_cal.insert("1.0",cal_content)
    text_cal.config(state="disabled")

    text_cal.grid(row=1,column=1,padx=20,pady=20)
    mainloop()

#creating the main entry window
window = Tk()
window.config(background="white")
window.title("CALENDAR")
window.geometry("250x250")

calenderlabel = Label(window,text = "CALENDAR",bg = "pink",fg = "blue",font=("Arial",30,"bold")).pack()
enteryear = Label(window,text = "ENTER YEAR",bg = "pink",fg = "blue",font=("Arial",15,"bold")).pack(pady=20)
entryear = Entry(window,font=("Arial",13,"bold"))
entryear.pack(pady=5)
showcalendar = Button(window,text="Show Calendar",width = 15,fg = "blue",bg="pink",command=showcal).pack(pady=5)
exit = Button(window,text="Exit",command=exit).pack(pady=5)


