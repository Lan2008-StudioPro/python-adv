import io
from PIL import Image, ImageTk
from tkinter import *


wd = Tk()
wd.title('Canva')
wd.geometry('1000x800')
wd.config(bg = '#DCFAFA')
wd.iconbitmap("20210822\w430.ico")


def resize(w, h, w_box, h_box, pil_image):
    fm1 = 1.0 * w_box / w
    fm2 = 1.0 * h_box / h
    fm = min([fm1, fm2])
    width = int(w * fm)
    height = int(h * fm)
    return pil_image.resize((width, height), Image.ANTIALIAS)

pil_image = Image.open(r'20210822/ether.gif')
w, h = pil_image.size
w_box = 400
h_box = 606
tk_image = ImageTk.PhotoImage(resize = (w, h, w_box, h_box, pil_image))

canva = Canvas(wd, width = 700, height = 700, bg = '#CBFAFA')
canva.pack()
cc = canva.create_oval(40, 70, 100, 130, fill = 'red', outline = 'red')
rangle = canva.create_rectangle(120, 34, 560, 78, fill = "blue", outline = "blue")
msg = canva.create_text(500, 400, text = "Yo", font = ('Arial', 24))


def move_canva(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canva.move(cc, 10, 0)
    elif key == "Left":
        canva.move(cc, -10, 0)
    elif key == "Up":
        canva.move(cc, 0, -10)
    elif key == "Down":
        canva.move(cc, 0, 10)


canva.bind_all('<Key>', move_canva)

'''
img = PhotoImage(file = "20210822\ether.gif")
imgs = canva.create_image(500, 400, image = img)
'''
  
wd.mainloop()