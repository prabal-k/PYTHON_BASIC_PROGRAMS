import pygame
import time
import random
pygame.init()

width=900
height=600
fps=60
window=pygame.display.set_mode(size=(width,height))
window.fill("red")

class ball:

    def __init__(self):
        self.x=450
        self.y=300
        self.radius=35
        self.xspeed=random.randint(-5,5)
        self.yspeed=random.randint(-5,5)
    def draw(self):
        pygame.draw.circle(surface=window,center=(self.x,self.y),radius=self.radius,color="white")

    def move(self):
        self.x=self.x+self.xspeed
        self.y=self.y+self.yspeed

    def boundarycollision(self):

        if(self.y+self.radius>height):
            self.yspeed=-self.yspeed

        if (self.y-self.radius < 0):
            self.yspeed = -self.yspeed


class rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def drawrect(self):
        pygame.draw.rect(window,"black",pygame.Rect(self.x1,self.y1,self.x2,self.y2))

#
run = True
clock = pygame.time.Clock()
ball_object=ball()               # creating  the ball

rectangle_object=rectangle(0,100,30,160)        # creating the 2 paddles/rectangles

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    window.fill(color="red")

    # creating and calling methods for ball

    ball_object.draw();
    ball_object.move()
    ball_object.boundarycollision()

    # creating and calling methods for rectangle/paddle

    rectangle_object.drawrect()

    pygame.display.update()

pygame.quit()

