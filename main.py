from tkinter import *
import math

root = Tk()

def click(event):
    global val
    ops=["(",")","/","*","+","-"]
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if val.get().isdigit():
            value = int(val.get())
        else:
            try:
                if "cos" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))*math.pi/180
                    value = round(math.cos(num),10)

                elif "sin" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))*math.pi/180
                    value = round(math.sin(num),10)

                elif "tan" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))*math.pi/180
                    calc = round(math.tan(num),10)
                    if calc>99999999999999:
                        value = "Undefined"
                    elif calc in [0.0,-0.0]:
                        value = 0
                    else:
                        value = calc

                elif "cot" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))*math.pi/180
                    calc = round(1/math.tan(num),10)
                    if calc>99999999999999:
                        value = "Undefined"
                    elif calc in [0.0,-0.0]:
                        value = 0
                    else:
                        value = calc

                elif "sec" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))*math.pi/180
                    calc = round(1/math.cos(num),10)
                    if calc>999999999999999:
                        value = "Undefined"
                    elif calc in [0.0,-0.0]:
                        value = 0
                    else:
                        value = calc

                elif "cosec" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))*math.pi/180
                    calc = round(1/math.sin(num),10)
                    if calc>999999999999999:
                        value = "Undefined"
                    elif calc in [0.0,-0.0]:
                        value = 0
                    else:
                        value = calc

                elif "log" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))
                    print(num)
                    if num<=0:
                        value = "Undefined"
                    else:
                        value = round(math.log(num),10)

                elif "sqrt" in scr.get():
                    num = eval(''.join(i for i in scr.get() if i.isdigit() or i in ops))
                    value = math.sqrt(num)

                else:
                    value = eval(scr.get())
            except ZeroDivisionError:
                value = "Undefined"
                print("Invalid Input")
            except Exception:
                value = "Invalid input"
                print("Invalid Input")

        val.set(value)
        scr.update()

    elif text == "C":
        val.set("")
        scr.update()

    else:
        val.set(val.get() + text)
        scr.update()


#visual
root.geometry("320x510+700+250")
root.minsize(320, 510)
root.maxsize(320, 510)
root.title("Calculator")
root.wm_iconbitmap('1.ico')

#input
val = StringVar()
val.set("")

#input textbox
scr = Entry(root, textvar=val, font="arial 25 bold")
scr.pack(fill=X, ipadx=5, padx=5, pady=12, anchor="n")

#internal visual
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

b = Button(f, text="cos", padx=20, pady=17, font="arial 15 bold")
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

b = Button(f, text="sin", padx=20, pady=17, font="arial 15 bold")
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

b = Button(f, text="tan", padx=20, pady=17, font="arial 15 bold")
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

b = Button(f, text="log", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)

f = Frame(root, bg="black")

b = Button(f, text="/", padx=22, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=19, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=20, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="cot", padx=20, pady=17, font="arial 15 bold")
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

b = Button(f, text=".", padx=21, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)

f = Frame(root, bg="black")

b = Button(f, text="sqrt", padx=19, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="sec", padx=23, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="cosec", padx=21, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="sec", padx=21, pady=17, font="arial 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack(padx=10)


root.mainloop()
