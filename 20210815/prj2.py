from tkinter import *

wd = Tk()
wd.title = ("prj")
wd.geometry("1000x800")
wd.config(bg = 'green')

def bgswap():
    pass

btn = Button(wd, text = 'Click Me', command = bgswap)
btn.pack()

wd.mainloop()

# Not Done Yet.