from tkinter import *

root = Tk()

canvas = Canvas(width=640, height=640, bg='blue')
canvas.pack()

photo = PhotoImage(file='C:\\Users\\User\\Desktop\\crpto 2.png')

canvas.create_image(0,0, image=photo, anchor=NW)



root.mainloop()
