# also added to github
import tkinter as tk

window=tk.Tk()

label=tk.Label(window,width=30,height=4,bg="white",font=("Ink free",20,"bold"))
label.pack()

frame=tk.Frame(window)
frame.pack()
number =""
num=""

# defining function:
def buttonpress(num):
    global number
    number=number+str(num)
    label.config(text=number)

def equal():
    try:
        global number
        total = str(eval(number))
        label.config(text=total)
        number=total
    except SyntaxError:
        label.config(text="Syntax error")
    except ZeroDivisionError:
        label.config(text="Error dividing by zero")

def clear():
    global number
    number=""
    label.config(text=number)


def one_clear():
    # length=len(number)
    global num
    global number
    num=number[:-1]
    label.config(text=num)
    number=num



# buttons
button_0=tk.Button(frame,text=0,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(0),activebackground="red")
button_0.grid(row=1,column=0)

button_1=tk.Button(frame,text=1,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(1),activebackground="red")
button_1.grid(row=1,column=1)

button_2=tk.Button(frame,text=2,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(2),activebackground="red")
button_2.grid(row=1,column=2)

button_3=tk.Button(frame,text=3,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(3),activebackground="red")
button_3.grid(row=2,column=0)

button_4=tk.Button(frame,text=4,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(4),activebackground="red")
button_4.grid(row=2,column=1)

button_5=tk.Button(frame,text=5,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(5),activebackground="red")
button_5.grid(row=2,column=2)

button_6=tk.Button(frame,text=6,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(6),activebackground="red")
button_6.grid(row=3,column=0)

button_7=tk.Button(frame,text=7,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(7),activebackground="red")
button_7.grid(row=3,column=1)

button_8=tk.Button(frame,text=8,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(8),activebackground="red")
button_8.grid(row=3,column=2)

button_9=tk.Button(frame,text=9,width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress(9),activebackground="red")
button_9.grid(row=4,column=0)

button_sum=tk.Button(frame,text="+",width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress("+"),activebackground="red")
button_sum.grid(row=4,column=1)

button_diff=tk.Button(frame,text="-",width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress("-"),activebackground="red")
button_diff.grid(row=4,column=2)

button_mult=tk.Button(frame,text="*",width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress("*"),activebackground="red")
button_mult.grid(row=5,column=0)

button_div=tk.Button(frame,text="/",width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress("/"),activebackground="red")
button_div.grid(row=5,column=1)

button_modulodiv=tk.Button(frame,text="%",width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress("%"),activebackground="red")
button_modulodiv.grid(row=5,column=2)

button_clear=tk.Button(frame,text="C",width=8,font=("Ink free",20,"bold"),command=clear,activebackground="red")
button_clear.grid(row=6,column=0)

button_equals=tk.Button(frame,text="=",width=8,font=("Ink free",20,"bold"),command=equal,activebackground="red")
button_equals.grid(row=6,column=1)

button_c=tk.Button(frame,text="<=",width=8,font=("Ink free",20,"bold"),command=one_clear,activebackground="red")
button_c.grid(row=6,column=2)

button_dot=tk.Button(frame,text=".",width=8,font=("Ink free",20,"bold"),command=lambda :buttonpress("."),activebackground="red")
button_dot.grid(row=7,column=0)


window.mainloop()