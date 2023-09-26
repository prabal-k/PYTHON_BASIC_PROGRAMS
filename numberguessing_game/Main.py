# i am inside main branch
import tkinter as tk
import random
window=tk.Tk()

number=""
chance=5
window.geometry("600x600")

welcome_label = tk.Label(window,text="Welcome to the word guessing game",font=("Ink free",30),bg="black",fg="white")
welcome_label.pack()

frame= tk.Frame(window)
frame.pack()
random_numlabel = tk.Label(frame,text="number is ", font=("Ink free", 30))
random_numlabel.grid(row=1,column=0,columnspan=2)


def display():
    global number
    number = random.randint(0, 100)
    random_numlabel.config(text=f"number is {number}")
    label.config(text="")

def checkguess():
    global number
    global chance
    try:
        guess=input_entry.get()
        guess=int(guess)
        if chance>=0:
            if guess >-1 and guess<100 :
                if guess==number:
                    label.config(text=f"Congratulation your guess is correct .Number is {number}",fg="green")
                    chance=5
                elif(guess>number):
                    chance=chance-1
                    label.config(text="your guess is high")
                elif (guess < number):
                    chance=chance-1
                    label.config(text="your guess is low")
            else:
                label.config(text="Guess between (0-100)")
        else:
            label.config(text=f"Game over number was {number}.Again press the generate number button",font=(10))
            chance=5
    except ValueError and TypeError and ValueError:
        label.config(text="Generate a number and then Guess a number ",fg="red")
    finally:
        chance_label.config(text=f"Chance left {chance}",fg="green")



generate_randombutton=tk.Button(frame,text="Generate number",command=display,font=('Arial',20,"bold"),fg="blue",activeforeground="blue")
generate_randombutton.grid(row=0,column=0,columnspan=2)

guess_label=tk.Label(frame,text="Enter your guess: ",font=("Ink free",30))
guess_label.grid(row=3,column=0)

input_entry = tk.Entry(frame)
input_entry.grid(row=3,column=1)

submit_button = tk.Button(frame,text="Submit",command=checkguess,font=('Arial',20,"bold"),fg="blue",activeforeground="blue")
submit_button.grid(row=5,column=0,columnspan =2)

label = tk.Label(frame,font=('Arial',16,"bold"),fg="red")
label.grid(row=6,column=0,columnspan =2)

chance_label=tk.Label(frame,text=f"Chance left {chance}",font=('Arial',20,"bold"),fg="green")
chance_label.grid(row=4,column=0,columnspan=2)




window.mainloop()