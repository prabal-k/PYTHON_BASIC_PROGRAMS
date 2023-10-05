import random
import tkinter as tk

window=tk.Tk()
# label to display tiktaktoe at the top
label = tk.Label(window,text="TikTaKToe",font=("Ink free",30,"bold"))
label.pack()

# to determine the random player to start
players=["X","O"]
player=random.choice(players)
player_label = tk.Label(window,text=f"{player} turn",font=("consolas",20))
player_label.pack()

frame=tk.Frame(window)
frame.pack()
list=[]

def checkwin(list):
   # print(list)
   for item in list:
       x=item.split(" ")
       for y in x:
           print(y)



def buttonpress(row,column):
    global player
    button[row][column]["text"] = player
    if player=="O":
        player="X"
    elif player == "X":
        player = "O"
    player_label.config(text=f"{player} turn")
    list.append(str(row)+str(column)+" "+button[row][column]["text"])

    checkwin(list)



button=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for row in range(0,3):
    for column in range(0,3):
        button[row][column]=tk.Button(frame,text="",width=20,height=6,command=lambda row=row,column=column:buttonpress(row,column),font=("Ink free",20,"bold"))
        button[row][column].grid(row=row,column=column)



window.mainloop()