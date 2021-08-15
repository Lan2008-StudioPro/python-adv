from tkinter import * # qt is also one way of it
# GUI - Graphic User Interface
import time

wd = Tk()
wd.geometry("1000x800")
wd.title("FrostFandom")
wd.configure(bg = '#B0B0FF')

def explode():
    timeout = 5
    while timeout == 0:
        print("Timeout activate! {} seconds...".format(timeout))
        time.wait(1)
        timeout -= 1
    display = Label(wd, text = "Enjoy", fg = "#12864a", bg = "#B0B100")
    display.pack()

bn1 = Button(wd, text = "Hg(CHO)₂",fg = "red", bg = "#B0B100", command = explode)
bn1.pack()

img = PhotoImage(file = "C:/Users/ASUS/Desktop/ether.gif")
img1 = Label(wd, image = img)
img1.pack()

wd.mainloop()

