import tkinter as tk


window=tk.Tk()

canvas=tk.Canvas(window,width=500,height=500,background="#346beb")
canvas.pack()
x1=y1=x2=y2=0
oval=""

def createoval(event):
    global x1,x2,y1,y2
    global oval
    x1=event.x - 20
    y1=event.y - 20
    x2=x1+40
    y2=y1+40
    oval=canvas.create_oval(x1, y1, x2, y2, outline="black", fill="#eb3462", width=2)
    
    print(type(oval))

def update():
    print("prabal")
    global oval,y1,y2
    y1+=2
    y2+=2
    canvas.coords(oval,x1,y1,x2,y2)         # Update oval position
    canvas.after(10,update)             # Schedule the next update after approximately 10ms


# adding mouse listner
window.bind("<Button-1>",createoval)
update()
window.mainloop()