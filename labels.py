import tkinter as tk

window = tk.Tk()
window.minsize(width=500,height=500)
window.config(bg="#5cfcff")

# for buttons
photo=tk.PhotoImage(file="C:\\Users\\Prabal Kuinkel\\Desktop\\4TH SEM BIT\\JAVA GAME\\src\\enemybullet.png")
def check():
    print("k xa hau")

button1= tk.Button(window,
                   text="Press me",
                   fg="Black",
                   bg="Blue",
                   font=("Ink free",20,"italic"),
                   activeforeground="Black",
                   activebackground="Blue",
                   compound="bottom",
                   command=check)
button1.pack()

# for CHECKBUTTON
def display():

    if(x.get()==1):
        print("you agree")

    else:
        print("you disgareed")

x=tk.IntVar()
print(x.get())
check_button=tk.Checkbutton(window,
                            text="i agree",
                            variable=x,
                            onvalue=1,
                            offvalue=0,
                            command=display
                            )
check_button.pack()

window.mainloop()