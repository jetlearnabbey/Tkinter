from tkinter import *
from tkinter.colorchooser import askcolor

class Painter:
    def __init__(self):
     self.window = Tk()

     self.draw = Button(self.window,text="Pen",commnd=None)
     self.draw.grid(row=0,column=0)

     self.color = Button(self.window,text="Color",command=None)
     self.color.grid(row=0,column=1)

     self.erase = Button(self.window,text="Erase",command=None)
     self.erase.grid(row=0,column=2)

     self.scale = Scale(self.window,from_=1,to=10,orient=HORIZONTAL)
     self.scale.grid(row=0,column=3)

     self.colorwheel = Canvas(self.window,bg="white",width=600,height=600)
     self.colorwheel.grid(row=1,columnspan=4)
