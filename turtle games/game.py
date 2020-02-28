from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')


p1 = StringVar()
p2 = StringVar()
pa = StringVar()
click = True
flag = 0


def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def win():

    if b1["text"] == b2["text"] == b3["text"] == "X" != 0 or \
            b4["text"] == b5["text"] == b6["text"] == "X" != 0 or \
            b7["text"] == b8["text"] == b9["text"] == "X" != 0 or\
            b1["text"] == b5["text"] == b9["text"] == "X" != 0 or\
            b3["text"] == b5["text"] == b7["text"] == "X" != 0 or \
            b1["text"] == b4["text"] == b7["text"] == "X" != 0 or \
            b2["text"] == b5["text"] == b8["text"] == "X" != 0 or \
            b3["text"] == b6["text"] == b9["text"] == "X" != 0:
        disable()
        messagebox.showinfo("information", p1.get() + " win")
    elif b1["text"] == b2["text"] == b3["text"] == "O" != 0 or \
            b4["text"] == b5["text"] == b6["text"] == "O" != 0 or \
            b7["text"] == b8["text"] == b9["text"] == "O" != 0 or\
            b1["text"] == b5["text"] == b9["text"] == "O" != 0 or\
            b3["text"] == b5["text"] == b7["text"] == "O" != 0 or \
            b1["text"] == b4["text"] == b7["text"] == "O" != 0 or \
            b2["text"] == b5["text"] == b8["text"] == "O" != 0 or \
            b3["text"] == b6["text"] == b9["text"] == "O" != 0:
        disable()
        messagebox.showinfo("information", p2.get() + " win")
    elif flag == 8:
        messagebox.showinfo("information", "it's a tie")


def btnclick(button):
    global click, p1, p2, flag
    if button["text"] == " " and click==True:
        button["text"] = "X"
        click = False
        win()
        flag += 1
    elif button["text"] == " " and click==False:
        click = True
        button["text"] = "O"
        win()
        flag += 1
    else:
        messagebox.showinfo("error", "button is already taken")


l1 = Label(root, text="player 1:")
l1.grid(row=0, column=0)

l2 = Label(root, text="player 2:")
l2.grid(row=1, column=0)

E1 = Entry(root, textvariable=p1)
E1.grid(row=0, column=1)

E2 = Entry(root, textvariable=p2)
E2.grid(row=1, column=1)

b1 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b1))
b1.grid(row=3, column=0)

b2 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b2))
b2.grid(row=3, column=1)

b3 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b3))
b3.grid(row=3, column=2)

b4 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b4))
b4.grid(row=4, column=0)

b5 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b5))
b5.grid(row=4, column=1)

b6 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b6))
b6.grid(row=4, column=2)

b7 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b7))
b7.grid(row=5, column=0)

b8 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b8))
b8.grid(row=5, column=1)

b9 = Button(root, text=" ", bg="white", padx=35, pady=35, command=lambda: btnclick(b9))
b9.grid(row=5, column=2)


root.mainloop()
