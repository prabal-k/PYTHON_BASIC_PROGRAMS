import tkinter as tk


window=tk.Tk()

canvas=tk.Canvas(window,width=500,height=500,background="#346beb")
canvas.pack()

def createoval(event):
    x1=event.x-20
    y1=event.y-20
    x2=x1+40
    y2=y1+40
    canvas.create_oval(x1, y1, x2, y2, outline="black", fill="#eb3462", width=2)





# adding mouse listner
window.bind("<Button-1>",createoval)
window.mainloop()