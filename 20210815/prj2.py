from tkinter import *

wd = Tk()
wd.title = ("prj")

def switch(lista):
    fg = lista[0]
    bg = lista[1]
    display = Label(wd, text = fg, fg = fg, bg = bg)
    display.pack()
    lista = reversed(lista)
    
btn = Button(wd, text = "Click me", command = switch(lista))
btn.pack()

wd.mainloop()