import tkinter as tk
import random

window=tk.Tk()
canvas=tk.Canvas(window,width=500,height=500,background="#66f542")
canvas.pack()
x1=y1=x2=y2=x=y=0
oval=""
def generateoval():
    global x1,x2,y1,y2,x,y,oval
    x1=random.randint(0,400)
    y1 = random.randint(0, 400)
    x=random.randint(0,180)
    x2=x1+x
    y2=y1+x
    print("x=",x,"x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2);
    oval=canvas.create_oval(x1,y1,x2,y2,fill="blue")

def fps():
    global x1,y1,x2,y2
    i=random.randint(-1,1)
    y1+=i
    y2+=i
    x1 += i
    x2 += i
    canvas.coords(oval,x1-i,y1-i,x2+i,y2+i)
    window.after(60,fps)

generateoval()
fps()
window.mainloop()