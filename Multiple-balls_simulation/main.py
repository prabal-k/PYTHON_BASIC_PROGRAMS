import tkinter as tk
import random
# from shutil import move

xpos=0
ypos=0

def changeposition(event):
    global xpos, ypos
    xpos = event.x
    ypos = event.y
    print(xpos, " ", ypos)
class simulaion:

    oval=""
    def __init__(self,color):
        self.x1 = random.randint(-500, 1000)
        self.y1= random.randint(-500,1000)
        self.x=random.randint(0,40)
        self.x2=self.x1+self.x
        self.y2=self.y1+self.x
        self.color=color

    def draw(self):
        self.oval=canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill=self.color,outline="")

    def move(self):
        global xpos,ypos
        z=2
        if xpos == 0 and ypos == 0:
            i=random.randint(-1,1)
            j = random.randint(-2, 2)
            self.y1 += i
            self.y2 += i
            self.x1 += j
            self.x2 += j
            canvas.coords(self.oval, self.x1, self.y1, self.x2, self.y2)

        else:
            if self.x1<xpos and self.x2<xpos:
                self.x1 +=z
                self.y1 +=z
                self.x2 += z
                self.y2 += z
            if self.x1 > xpos and self.x2 > xpos:
                self.x1 -= z
                self.y1 -= z
                self.x2 -= z
                self.y2 -= z

            # if self.y1<ypos and self.y2>ypos:
            #     self.x1+=z
            #     self.y1+=z
            #     self.x2 += z
            #     self.y2 += z
            #
            # if self.x1>xpos and self.y1>ypos:
            #     self.x1 -= z
            #     self.y1 -= z
            #     self.x2 -= z
            #     self.y2 -= z


            # elif self.x1==xpos:
            #     i = random.randint(-200, 200)
            #     j = random.randint(-200, 200)
            #     self.y1 += i
            #     self.y2 += i
            #     self.x1 += j
            #     self.x2 += j

            canvas.coords(self.oval, self.x1, self.y1, self.x2, self.y2)

        window.after(60, self.move)



window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=600, background="black")
canvas.pack()

# for mouse events



particlesarrayr=[]
for i in range(0,850):
    object=simulaion("green")
    particlesarrayr.append(object)

for i in range(0,850):
    particlesarrayr[i].draw()
    particlesarrayr[i].move()

window.bind("<Button-1>",changeposition)





# object2=simulaion()
# object2.draw()
# object2.move()
#
# object3=simulaion()
# object3.draw()
# object3.move()

window.mainloop()
