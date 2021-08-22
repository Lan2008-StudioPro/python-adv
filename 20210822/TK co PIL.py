from tkinter import *
from PIL import Image as Ima
from PIL import ImageTk

wd = Tk()
wd.title("Test_Module")
wd.geometry('1000x800')
wd.config(bg = '#DCFAFA')
wd.iconbitmap("20210822\ether.ico")

# Resize Tutorial

'''
def resize(w, h, w_box, h_box, pil_image):
    fm1 = 1.0 * w_box / w
    fm2 = 1.0 * h_box / h
    fm = min([fm1, fm2])
    width = int(w * fm)
    height = int(h * fm)
    return pil_image.resize((width, height), Ima.ANTIALIAS)

pil_image = Ima.open("20210822/ether.gif")
w, h = pil_image.size
w_box = 100
h_box = 100
tk_image = ImageTk.PhotoImage(resize(w, h, w_box, h_box, pil_image))
Label_0 = Label(wd, image = tk_image, width = w_box, height = h_box)
Label_0.pack(padx = 10, pady = 10)
'''

# Width and height is for the text inside the Label. 

'''
Label_1 = Label(wd, text = 'Hi! Welcome to FrostFandom.', 
    fg = 'Violet', bg = '#C580B3', font = ('Arial', 14), width = 30, height = 2)
Label_1.pack()
'''
# Same for the Button.

var_2 = StringVar()
Label_2 = Label(wd, textvariable = var_2, bg = '#C9FFFF', fg = 'green',
    width = 30, height = 2, font = ('Arial', 28))
Label_2.pack()

timers_var = False
def press():
    global timers_var
    if timers_var == False:
        timers_var = True
        var_2.set('Ouch')
    else:
        timers_var = False
        var_2.set('')

Button_1 = Button(wd, text = 'Press me.', fg = 'red', font = ('Arial', 16), width = 10, height = 1, command = press)
Button_1.pack(side = 'top')


wd.mainloop()