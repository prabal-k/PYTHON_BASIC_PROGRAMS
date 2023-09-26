# widgets = GUI elements like :Buttons ,textbox,labels,images
# windows = Server as a container to hold or contain these widgets

import tkinter

window=tkinter.Tk()
window.geometry("600x600")
window.title("first GUI")

# to change the image icon of the window
icon = tkinter.PhotoImage(file="groundenemy.gif")
window.iconphoto(True,icon)
# -------

window.config(background="#5cfcff")  # to change the background color of the window
# LABELS
photo = tkinter.PhotoImage(file="groundenemy.gif")
label1=tkinter.Label(window,text="hello world",
                     font=("Ink free",40,"bold"),
                     fg="#00FF00",
                     bg="black",
                     image=photo,
                     compound='top')
# label1.place(x=0,y=0)
label1.pack()
# to add image on the label
#BUTTIONS
count=0

def working():
    name=entry.get();
    print(name)
    label=tkinter.Label(window,text="Hello "+name,
                        font=("Arial",20))
    label.pack()

photo1=tkinter.PhotoImage(file="car.png")
butt=tkinter.Button(window,
                    text="click me",
                    font=("Ink free",20,"bold"),
                    image=photo1,
                    compound="bottom",
                    fg="white",
                     bg="black",
                    command=working,
                    activeforeground="white",
                    activebackground="black"
                    )
butt.pack()

# entry -- take input from the user


entry = tkinter.Entry(window,
                      bg="black",
                      fg="white",
                      font=("Ink free",30,"bold"))

entry.pack()
window.mainloop()                                   # makes the window visible on the screen



