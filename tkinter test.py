from tkinter import *

window = Tk()
canvas = Canvas(window,bg = "black",height=500,width=500)
canvas.create_line(0,0,500,500,fill = "white")
canvas.create_line(0,250,500,250,fill = "white")
canvas.create_line(250,0,250,500,fill = "white")
canvas.create_line(500,0,0,500,fill = "white")
canvas.pack()
window.mainloop()