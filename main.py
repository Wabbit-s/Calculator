from tkinter import *

root = Tk()

def click(event):
    global val
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if val.get().isdigit():
            value = int(val.get())
        else:
            value = eval(scr.get())

        val.set(value)
        scr.update()

    elif text == "C":
        val.set("")
        scr.update()

    else:
        val.set(val.get() + text)
        scr.update()



root.geometry("280x440")
root.minsize(280, 440)
root.title("Calculator")
root.wm_iconbitmap('1.ico')


val = StringVar()
val.set("")
scr = Entry(root, textvar=val, font="arial 25 bold")
scr.pack(fill=X, ipadx=5, padx=5, pady=12, anchor="n")


f = Frame(root, bg="black")

b = Button(f, text="9", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)


f = Frame(root, bg="black")

b = Button(f, text="6", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)

f = Frame(root, bg="black")

b = Button(f, text="3", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)

f = Frame(root, bg="black")

b = Button(f, text="0", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=22, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=22, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)

f = Frame(root, bg="black")

b = Button(f, text="/", padx=22, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=18, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)

f = Frame(root, bg="black")

b = Button(f, text="C", padx=19, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="(", padx=23, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=")", padx=21, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)


root.mainloop()