from tkinter import *

wdw = Tk()
wdw.title("prj") 
img = PhotoImage(file = "C:/Users/ASUS/Desktop/ether.gif")
wdw.configure(bg = "#12864a")

def swap():
    wdw.destroy()

def surprise():
    dp = Label(wdw, text = "HI", fg = "#57302c")
    dp.pack()

btn_txt = Button(wdw, text = "Bomb", fg = "red", bg = "#B0B100", command = surprise)
btn_txt.pack()

btn_die = Button(wdw, text = "Destroyer", command = swap)
btn_die.pack()

wdw.mainloop()