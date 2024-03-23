import math

import pygame
import random
pygame.init()
width=800
height=800
window=pygame.display.set_mode((width,height))           #  setting the window to appear on the screen
pygame.display.set_caption("first pygame")               # set the title of window


color="#3efa7a"
fps=60
ballcoount=4
# main function

# coordinates of the circle

class circle:
    def __init__(self):
        self.xpos = random.randint(100,500)
        self.ypos = random.randint(100,500)
        self.radius = random.randint(20, 60)
        self.xspeed = random.randint(-5, 5)
        self.yspeed = random.randint(-5, 5)

    def draw(self):
        pygame.draw.circle(window, center=(self.xpos, self.ypos), radius=self.radius, color="blue")

    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed

    def boundary_collision(self):
        if (self.xpos + self.radius >= width) or (self.xpos - self.radius <= 0):
            self.xspeed = -self.xspeed

        if (self.ypos + self.radius >= height) or (self.ypos - self.radius <= 0):
            self.yspeed = -self.yspeed

    def collision(self,ballobject):
        for item in ballobject:
            if item!=self:
                x=self.xpos-item.xpos
                y=self.ypos-item.ypos
                distance=math.sqrt(math.pow(x,2)+math.pow(y,2))
                if(distance<self.radius+item.radius):
                    # self.xspeed=-self.xspeed
                    # self.yspeed=-self.yspeed
                    # item.xspeed = -item.xspeed
                    # item.yspeed = -item.yspeed
                         # Swap the speeds of the two circles
                    self.xspeed, item.xspeed = item.xspeed, self.xspeed
                    self.yspeed, item.yspeed = item.yspeed, self.yspeed




ball_object=[]
for i in range (0,ballcoount):
    circle_obj = circle()
    ball_object.append(circle_obj)

clock=pygame.time.Clock()
run=True
while run:                                          # to appear the window on the screen
    clock.tick(fps)
    for event in pygame.event.get():                # get the event
        if event.type==pygame.QUIT:                 # if user presses the close button on the window =>close the window
            run=False
    window.fill("red")  # each time one frame is draw,move and checked colliision the screen is cleared for each frame

    for i in range(0,ballcoount):
        ball_object[i].draw()
        ball_object[i].move()
        ball_object[i].boundary_collision()
        ball_object[i].collision(ball_object)
    # pygame.draw.circle(surface=window,center=(0,0),radius=10,color="blue");

    pygame.display.update()



pygame.quit()



