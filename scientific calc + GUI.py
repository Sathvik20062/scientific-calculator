from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

switch = None


def btn1():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0():
    if disp.get == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get == '0':
        disp.delete(0, END)


def btnp():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnm():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnmlt():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc():
    disp.delete(0, END)
    disp.insert(0, 'c')


def sin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def cos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def tan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def arcsin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def arccos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def arctan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def pow():
    pos=len(disp.get())
    disp.insert(pos, '**')


def rnd():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def logarithm():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def fact():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def sqr():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def dot():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def e():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def bl():
    pos = len(disp.get())
    disp.insert(pos, '(')


def br():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_btn():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def conv():
    global switch
    if switch is None:
        switch = True
        conv_btn['Text'] = "Deg"
    else:
        switch = None
        conv_btn['Text'] = "Rad"


def ln():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def mod():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btneq():
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


data = StringVar()

disp = Entry(root, font="Verdana 20", fg="black", bg="#abbab1", bd=0, justify= RIGHT, insertbackground="#abbab1",
             cursor="arrow")
disp.bind("<Return>", btneq)
disp.bind("<Escape>", btnc)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, "")
disp.focus_set()
disp.pack(expand=True, fill=BOTH)

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Segoe 23", relief=FLAT, bd=0, command=pi, fg="black",
                highlightbackground="#333333", height=1, width=1)
pi_btn.pack(side=LEFT, expand=True, fill=BOTH)

fact_btn = Button(btnrow1, text="x!", font="Segoe 23", relief=FLAT, bd=0, command=fact,
                  highlightbackground="#333333", height=1, width=1)
fact_btn.pack(side=LEFT, expand=True, fill=BOTH)

sin_btn = Button(btnrow1, text="Sin", font="Segoe 23", relief=FLAT, bd=0, command=sin, fg="black",
                 highlightbackground="#333333", height=1, width=1)
sin_btn.pack(side=LEFT, expand=True, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Segoe 23", relief=FLAT, bd=0, command=cos, fg="black",
                 highlightbackground="#333333", height=1, width=1)
cos_btn.pack(side=LEFT, expand=True, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font=("Segoe", "23"), relief=FLAT, bd=0, command=tan, fg="black",
                 highlightbackground="#333333", height=1, width=1)
tan_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 23", relief=FLAT, bd=0, command=btn1, fg="black", height=1, width=1)
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 23", relief=FLAT, bd=0, command=btn2, fg="black", height=1, width=1)
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 23", relief=FLAT, bd=0, command=btn3, fg="black", height=1, width=1)
btn3.pack(side=LEFT, expand=True, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Segoe 23", relief=FLAT, bd=0, command=btnp, fg="black",
              highlightbackground="#333333", height=1, width=1)
btnp.pack(side=LEFT, expand=True, fill=BOTH)


btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill=BOTH)

e_btn = Button(btnrow2, text="e", font=("Segoe", "23"), relief=FLAT, bd=0, command=e, fg="black",
               highlightbackground="#333333", height=1, width=1)
e_btn.pack(side=LEFT, expand=True, fill=BOTH)

sqr_btn = Button(btnrow2, text="√x", font=("Segoe", "23"), relief=FLAT, bd=0, command=sqr, fg="black",
                 highlightbackground="#333333", height=1, width=1)
sqr_btn.pack(side=LEFT, expand=True, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin-1", font=("Segoe", "23"), relief=FLAT, bd=0, command=arcsin, fg="black",
                  highlightbackground="#333333", height=1, width=1)
sinh_btn.pack(side=LEFT, expand=True, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font=("Segoe", "23"), relief=FLAT, bd=0, command=arccos, fg="black",
                  highlightbackground="#333333", height=1, width=1)
cosh_btn.pack(side=LEFT, expand=True, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font=("Segoe", "23"), relief=FLAT, bd=0, command=arctan, fg="black",
                  highlightbackground="#333333",height=1, width=1)
tanh_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Segoe 23", relief=FLAT, bd=0, command=btn4, fg="black", height=1, width=1)
btn4.pack(side=LEFT, expand=True, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 23", relief=FLAT, bd=0, command=btn5, fg="black", height=1, width=1)
btn5.pack(side=LEFT, expand=True, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Segoe 23", relief=FLAT, bd=0, command=btn6, fg="black", height=1, width=1)
btn6.pack(side=LEFT, expand=True, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Segoe 25", relief=FLAT, bd=0, command=btnm, fg="black",
              highlightbackground="#333333", height=1, width=1)
btnm.pack(side=LEFT, expand=True, fill=BOTH)


btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill=BOTH)

conv_btn = Button(btnrow3, text="Rad", font="Segoe 23", relief=FLAT, bd=0, command=conv, fg="black",
                  highlightbackground="#333333", height=1, width=1)
conv_btn.pack(side=LEFT, expand=True, fill=BOTH)

rnd_btn = Button(btnrow3, text="Rnd", font=("Segoe", "23"), relief=FLAT, bd=0, command=rnd, fg="black",
                 highlightbackground="#333333", height=1, width=1)
rnd_btn.pack(side=LEFT, expand=True, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font=("Segoe", "23"), relief=FLAT, bd=0, command=ln, fg="black",
                highlightbackground="#333333", height=1, width=1)
ln_btn.pack(side=LEFT, expand=True, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Segoe 23", relief=FLAT, bd=0, command=logarithm,
                       highlightbackground="#333333", height=1, width=1)
logarithm_btn.pack(side=LEFT, expand=True, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Segoe 23", relief=FLAT, bd=0, command=pow, fg="black",
                 highlightbackground="#333333", height=1, width=1)
pow_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 23", relief=FLAT, bd=0, command=btn7, fg="black", height=1, width=1)
btn7.pack(side=LEFT, expand=True, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 23", relief=FLAT, bd=0, command=btn8, fg="black", height=1, width=1)
btn8.pack(side=LEFT, expand=True, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 23", relief=FLAT, bd=0, command=btn9, fg="black", height=1, width=1)
btn9.pack(side=LEFT, expand=True, fill=BOTH)

btnmlt = Button(btnrow3, text="*", font="Segoe 23", relief=FLAT, bd=0, command=btnmlt, fg="black",
                highlightbackground="#333333", height=1, width=1)
btnmlt.pack(side=LEFT, expand=True, fill=BOTH)


btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Segoe 23", relief=FLAT, bd=0, command=mod, fg="black",
                 highlightbackground="#333333", height=1, width=1)
mod_btn.pack(side=LEFT, expand=True, fill=BOTH)

bl_btn = Button(btnrow4, text="(", font="Segoe 23", relief=FLAT, bd=0, command=bl, fg="black",
                highlightbackground="#333333", height=1, width=1)
bl_btn.pack(side=LEFT, expand=True, fill=BOTH)

br_btn = Button(btnrow4, text=")", font="Segoe 23", relief=FLAT, bd=0, command=br, fg="black",
                highlightbackground="#333333", height=1, width=1)
br_btn.pack(side=LEFT, expand=True, fill=BOTH)

del_btn = Button(btnrow4, text="Del", font="Segoe 23", relief=FLAT, bd=0, command=del_btn, fg="black",
                 highlightbackground="#333333", height=1, width=1)
del_btn.pack(side=LEFT, expand=True, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Segoe 23", relief=FLAT, bd=0, command=btnc, fg="black",
              highlightbackground="#333333", height=1, width=1)
btnc.pack(side=LEFT, expand=True, fill=BOTH)

dot_btn = Button(btnrow4, text=".", font="Segoe 23", relief=FLAT, bd=0, command=dot, fg="black",
                 highlightbackground="#333333", height=1, width=1)
dot_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=FLAT, bd=0, command=btn0, fg="black", height=1, width=1)
btn0.pack(side=LEFT, expand=True, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", relief=FLAT, bd=0, command=btneq, fg="black",
               highlightbackground="#333333", height=1, width=1)
btneq.pack(side=LEFT, expand=True, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 23", relief=FLAT, bd=0, command=btnd, fg="black",
              highlightbackground="#333333", height=1, width=1)
btnd.pack(side=LEFT, expand=True, fill=BOTH)


root.mainloop()
