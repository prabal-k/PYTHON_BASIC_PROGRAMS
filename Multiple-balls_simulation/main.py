import tkinter as tk
import random
# from shutil import move


class simulaion:

    oval=""
    def __init__(self):
        self.x1 = random.randint(0, 550)
        self.y1= random.randint(0,550)
        self.x=random.randint(0,40)
        self.x2=self.x1+self.x
        self.y2=self.y1+self.x

    def draw(self):
        self.oval=canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill="blue",outline="")

    def move(self):
        i=random.randint(-1,1)
        j = random.randint(-2, 2)
        self.y1 += i
        self.y2 += i
        self.x1 += j
        self.x2 += j
        canvas.coords(self.oval,self.x1,self.y1,self.x2,self.y2)
        window.after(60, self.move)

window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=600, background="black")
canvas.pack()

particlesarrayr=[]
for i in range(0,250):
    object=simulaion()
    particlesarrayr.append(object)

for i in range(0,250):
    particlesarrayr[i].draw()
    particlesarrayr[i].move()



# object2=simulaion()
# object2.draw()
# object2.move()
#
# object3=simulaion()
# object3.draw()
# object3.move()

window.mainloop()
