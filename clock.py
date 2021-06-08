# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:14:57 2021

@author: KenYang
"""

from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text = time_string)
    
    day_string = strftime("%Y %B %d, %A")
    day_label.config(text = day_string)
    
    time_label.after(1000,update)

window = Tk()
window.config(bg="black")
window.title("Clock")
day_label = Label(window,font=("Times New Roman",20),fg="white",bg="black")
day_label.pack()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

update()


window.mainloop()
