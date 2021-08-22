from tkinter import *

wd = Tk()
wd.title = ("prj")

listnum = 0

def switch():
    global listnum
    if listnum == 0:
        listnum = 1
        dp = Label(wd, text = 'green', fg = 'green', bg = 'red')
    elif listnum == 1:
        listnum = 0
        dp = Label(wd, text = 'red', fg = 'red', bg = 'green')
    dp.pack()

btn = Button(wd, text = "Click me", command = switch)
btn.pack()

wd.mainloop()