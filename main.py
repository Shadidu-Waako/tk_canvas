from tkinter import *


my_window = Tk()
my_canvas_1 = Canvas(my_window, width=200, height=200, background='red')
my_canvas_2 = Canvas(my_window, width=200, height=200, background='orange')
my_canvas_3 = Canvas(my_window, width=200, height=200, background='yellow')
my_canvas_4 = Canvas(my_window, width=200, height=200, background='green')
my_canvas_1.grid(row=0, column=0)
my_canvas_2.grid(row=0, column=1)
my_canvas_3.grid(row=1, column=0)
my_canvas_4.grid(row=1, column=1)

my_window.mainloop()
