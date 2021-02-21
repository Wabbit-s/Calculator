from tkinter import *

root = Tk()

def click(event):
    global val
    text = event.widget.cget("text")
    if text == "=":
        pass
    elif text == "c":
        pass
    else:
        val.set(val.get() + text)
        scr.update()



root.geometry("512x480")
root.minsize(300,100)
root.title("Calculator")
root.wm_iconbitmap("icon.ico")


val = StringVar()
val.set("")
scr = Entry(root, textvar=val, font="arial 15 bold")
scr.pack(fill=X, ipadx=10, padx=5, pady=12)

f1 = Frame(root, bg="grey")
f1.pack()
f2 = Frame(root, bg="grey")
f2.pack()
f3 = Frame(root, bg="grey")
f3.pack()
f4 = Frame(root, bg="grey")
f4.pack()
b1 = Button(f1, text="9", padx=20, pady=20, font="arial 15 bold")
b1.pack(side=LEFT, padx=10, pady=12)
b1.bind("Button", click)
b2 = Button(f1, text="8", padx=20, pady=20, font="arial 15 bold")
b2.pack(side=LEFT, padx=10, pady=12)
b2.bind("Button", click)
b3 = Button(f1, text="7", padx=20, pady=20, font="arial 15 bold")
b3.pack(side=LEFT, padx=10, pady=12)
b3.bind("Button", click)
b4 = Button(f1, text="6", padx=20, pady=20, font="arial 15 bold")
b4.pack(side=LEFT, padx=10, pady=12)
b4.bind("Button", click)

root.mainloop()