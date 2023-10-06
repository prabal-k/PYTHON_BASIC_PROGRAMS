import tkinter as tk

def dosomething(event):
    print("mouse clicked at "+str(event.x)+","+str(event.y))

window=tk.Tk()
window.geometry("300x300")
# syntax for bind is window.bind(event,function)
window.bind("<Button-1>",dosomething)               #for left button click on mouse

# window.bind("<Button-2>",dosomething)             #for clicking on mouse wheel click

# window.bind("<Button-3>",dosomething)             #for right button click on mouse

# window.bind("<ButtonRelease>",dosomething)           # for when the mouse is reseased

# window.bind("<Enter>",dosomething)                      # for the position when i entered the window

# window.bind("<Leave>",dosomething)                     # for when I leave the window

# window.bind("<Motion>",dosomething)                     # where i move the mouse



window.mainloop()