import tkinter as tk
from tkinter import messagebox
from PIL import Image
from pygame import mixer
import re
import random


def getKey():
    return 0


def get_entry():
    entry = keyentry.get()
    if (len(entry)==6)and(re.match(r'\d\d\d\d\d\d', entry)):
        a = entry[3] + entry[4] + entry[5] + random.choice(letters) + random.choice(letters)
        b = entry[0] + entry[1] + entry[2] + random.choice(letters) + random.choice(letters)
        c = str(int(entry[3] + entry[4] + entry[5]) + int(entry[0] + entry[1] + entry[2]))
        messagebox.showinfo("Ваш ключ", a+" "+b+" "+c)
    else:
        messagebox.showerror("Ошибка", "Введите шестизначное число")
    keyentry.delete(0, len(entry))

def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(180, lambda: animation(count))


def stop_animation():
    root.after_cancel(anim)


letters = "ABCDEF"

mixer.init()
mixer.music.load('Theme.mp3')
mixer.music.play()

root = tk.Tk()

icon = tk.PhotoImage(file="icon.png")
root.title('Papers, Please - Key Generator')
root.iconphoto(False, icon)

file = "back3.gif"
info = Image.open(file)
frames = info.n_frames
im = [tk.PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None

gif_label = tk.Label(root, image="")
gif_label.pack()

keyentry = tk.Entry(root, font='Courier 30', width=6)
keyentry.place(x=527, y=460)

confirm = tk.Button(root, text='подтвердить ввод', command=get_entry, font='Courier 20',)
confirm.place(x=462, y=520)
canvas = tk.Canvas(root, width=1200, height=675)
back = tk.PhotoImage(file=r'back3.gif')
canvas.create_image(100, 100, image=back, anchor='nw')
animation(count)
root.mainloop()
