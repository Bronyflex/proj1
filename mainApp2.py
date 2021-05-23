import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
import re

# ClassName.__doc__


from tkinter import *
from math import sqrt


def solver(a,b,c):
    """ Solves quadratic equation and returns the result in formatted string """
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = " Дискрименант: %s \n х1: %s \n х2: %s \n" % (D, x1, x2)
    else:
        text = " Дискрименант: %s \n Нет Решения" % D
    return text

def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0","end")
    output.insert("0.0",value)

def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")

def handler():
    """ Get the content of entries and passes result to the text """
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Введены не все числа уравнения")

root = Tk()

root.title("Решение квадратного уравнения")

root.resizable(width=False, height=False)


frame = Frame(root, borderwidth=0)
frame.grid()
frame = Frame(root)
frame['bg'] = "black"
frame.grid()



a = Entry(frame, width=2,font="Arial 30")
a.grid(row=1, column=1)
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="x^2+",font="Arial 30",bg="black", fg="white").grid(row=1,column=2)

b = Entry(frame, width=2,font="Arial 30")
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+",font="Arial 30",bg="black", fg="white").grid(row=1, column=4)

c = Entry(frame, width=2,font="Arial 30")
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0",font="Arial 30",bg="black", fg="white").grid(row=1, column=6)

but = Button(frame, text="Решить",font="Arial 30",bg="black", fg="white",borderwidth=0, command=handler).grid(row=1, column=7 )

output = Text(frame, bg="black", font="Arial 20", width=35, height=4,fg="white", borderwidth=0)
output.grid(row=2, columnspan=8)

root.mainloop()