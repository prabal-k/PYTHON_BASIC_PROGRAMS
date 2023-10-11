import math
import tkinter as tk
import random
class balls:
    def __init__(self,canvas,color):
        self.x1 = random.randint(110,480)
        self.y1 = random.randint(110,480)
        self.r=random.randint(60,100)
        self.x2 = self.x1 + self.r
        self.y2 = self.y1 + self.r
        self.canvas=canvas
        self.oval=""
        self.xspeed=random.randint(-10,10)
        self.yspeed=random.randint(-10,10)
        self.color=color
        self.dx=0
        self.dy=0

    def draw(self):

        if self.oval:
            self.canvas.delete(self.oval)  # Remove the previous oval
        self.oval=self.canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill=self.color,outline=self.color)

    def movie(self):
        pass
        self.x1 += self.xspeed
        self.x2 += self.xspeed
        self.y1 += self.yspeed
        self.y2 += self.yspeed
    def collision(self,color):
        # print("ball-1",ballobject1.x1," ",ballobject1.y1)
        # print("ball-2",ballobject2.x1," ",ballobject2.y1)
        #
        # xdis=ballobject2.x1-ballobject1.x1
        # ydis=ballobject2.y1-ballobject1.y1
        # square=math.pow(xdis,2)+math.pow(ydis,2)
        # distance=math.sqrt(square)
        # print("distance = ",distance)
        # print(xdis," ",ydis)
        # if(distance<(ballobject1.x1-ballobject1.x2)):
        #     print("collision")
        if(ballobject1.x1 <ballobject2.x1 <ballobject1.x2) and(ballobject1.y1<ballobject2.y2<ballobject1.y2):
            ballobject2.xspeed=+4
            ballobject1.xspeed=-4

        if(ballobject1.x1<ballobject2.x2<ballobject1.x2) and(ballobject1.y1<ballobject2.y2<ballobject1.y2):
            ballobject2.xspeed=-4
            ballobject1.xspeed=4

        if(ballobject1.x1<ballobject2.x2<ballobject1.x2) and (ballobject1.y1<ballobject2.y1<ballobject1.y2):
            ballobject1.xspeed=4
            ballobject2.xspeed=-4

        if(ballobject1.x1<ballobject2.x1<ballobject1.x2) and (ballobject1.y1<ballobject2.y1<ballobject1.y2):
            ballobject1.xspeed=-4
            ballobject2.xspeed=+4





    def check(self):
        if(self.x2>600):
            self.xspeed=-self.xspeed
        if (self.y2 > 600):
            self.yspeed = -self.yspeed
        if(self.x1<0):
            self.xspeed=-self.xspeed

        if (self.y1<0):
            self.yspeed = -self.yspeed

    def fps(self):
        self.draw()
        self.collision(self.color)

        self.movie()
        self.check()
        window.after(16,self.fps)# 16 milliseconds for approximately 60 FPS

window=tk.Tk()
window.geometry("600x600")
canvas=tk.Canvas(window,width=600,height=600,background="black")
canvas.pack()

# creating objects
# ball_object=[]
# for i in range (0,5):
#     ball_obj=balls(canvas)
#     ball_object.append(ball_obj)
#
# for i in range(0,5):
#     ball_object[i].fps()

ballobject1=balls(canvas,"green")
ballobject2=balls(canvas,"blue")
# ballobject3=balls(canvas,"red")
# ballobject4=balls(canvas,"orange")

ballobject1.fps()
ballobject2.fps()
# ballobject3.fps()
# ballobject4.fps()

window.mainloop()