import random
from functools import partial
from tkinter import*


def change_label_number(num1):
    for j in range(num1):
        arr.append(PhotoImage(file=f"img1\\autumn_dise_1_{j + 1}.png"))
        random.shuffle(arr)
    for s in range(num1):
        Label(image=arr[s]).grid(row=1, column=i)


tk = Tk()
arr = []
num = 4
for i in range(num):
    arr.append(PhotoImage(file=f"img1\\autumn_dise_1_{i+1}.png"))
    random.shuffle(arr)
for i in range(num):
    Label(tk, image=arr[i]).grid(row=1, column=i)
Button(tk, text='Ок', command=partial(change_label_number, num)).grid(row=2, columnspan=num)
tk.mainloop()

