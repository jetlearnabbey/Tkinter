from tkinter import *
from tkinter.colorchooser import askcolor

class Painter:
    def __init__(self):
     self.window = Tk()

     self.draw = Button(self.window,text="Pen",command=self.usepen)
     self.draw.grid(row=0,column=0)

     self.color = Button(self.window,text="Color",command=self.colorchooser)
     self.color.grid(row=0,column=1)

     self.erase = Button(self.window,text="Erase",command=self.useraser)
     self.erase.grid(row=0,column=2)

     self.scale = Scale(self.window,from_=1,to=10,orient=HORIZONTAL)
     self.scale.grid(row=0,column=3)

     self.colorwheel = Canvas(self.window,bg="white",width=600,height=600)
     self.colorwheel.grid(row=1,columnspan=4)
     self.setup()

    def setup(self):
       self.x = None
       self.y = None
       self.linewidth = self.scale.get()
       self.color = "black"
       self.activebutton = self.draw
       self.colorwheel.bind('<B1-Motion>',self.paint)
       self.colorwheel.bind('<ButtonRelease-1>',self.reset)

    def colorchooser(self):
      self.color = askcolor(color=self.color)[1]

    def usepen(self):
       self.activatebutton(self.draw)
       self.color = "black" if self.color=="white" else self.color

    def useraser(self):
       self.activatebutton(self.erase)
       self.color="white"

    def activatebutton(self,but):
       self.activebutton.config(relief=RAISED)
       self.but.config(relief=SUNKEN)
       self.activebutton = but

    def paint(self,event):
         self.linewidth = self.scale.get()
         if self.x and self.y:
            self.colorwheel.create_line(self.x,self.y,event.x,event.y,width=self.linewidth,fill=self.color)
         self.x = event.x
         self.y = event.y

    def reset(self,event):
       self.x,self.y = None,None

       

       
       
       

       
          
    

       
       

Painter()

mainloop()
