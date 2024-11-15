from tkinter import *
import tkinter.font as font

def calculate_distance():
        time = float(time_entry.get())  
        speed = float(speed_entry.get())  
        distance = speed * time  
window = Tk()
window.title("Distance Calculator")
window.geometry("400x300")


title_label = Label(window, text="Distance Calculator", font=font.Font(size=18), fg="blue")
title_label.pack(pady=10)


input_frame = Frame(window)
input_frame.pack(pady=10)


time_label = Label(input_frame, text="Time (hours):", font=font.Font(size=12))
time_label.grid(row=0, column=0, padx=10, pady=5)
time_entry = Entry(input_frame, font=font.Font(size=12))
time_entry.grid(row=0, column=1, padx=10, pady=5)


speed_label = Label(input_frame, text="Speed (units/hour):", font=font.Font(size=12))
speed_label.grid(row=1, column=0, padx=10, pady=5)
speed_entry = Entry(input_frame, font=font.Font(size=12))
speed_entry.grid(row=1, column=1, padx=10, pady=5)


calculate_button = Button(window, text="Calculate Distance", bg="orange", font=font.Font(size=12), command=calculate_distance)
calculate_button.pack(pady=10)

result_label = Label(window, text="Distance Covered:4", font=font.Font(size=12), fg="green")
result_label.pack(pady=10)


window.mainloop()
