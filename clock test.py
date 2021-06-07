from tkinter import *
from time import *

def update():
    timestr = strftime("%I:%M:%S %p")
    time_label.config(text=timestr)

    window.after(100,update)

window = Tk()
window.config(bg="black")
time_label = Label(window,font=("Arial",30),fg="#00FF00",bg="black")
time_label.place(x=0,y=0)
time_label.pack()
update()
window.mainloop()