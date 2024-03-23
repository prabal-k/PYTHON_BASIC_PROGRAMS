import pygame
import random
pygame.init()

width=900
height=600
fps=60
window=pygame.display.set_mode(size=(width,height))
window.fill("red")

class ball:
    def __init__(self):
        self.x=width/2
        self.y=height/2
        self.radius=35
        self.number=random.randint(0,1)
        if self.number==0:
            self.xspeed=-5
            self.yspeed=5
        else:
            self.xspeed = 5
            self.yspeed = 5

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
        self.inc=4;

    def drawrect(self):
        pygame.draw.rect(window,"black",pygame.Rect(self.x1,self.y1,self.x2,self.y2))

    def downmovement(self):
            self.y1+=self.y1
            self.y2+=self.y2

    def upmovement(self):
            self.y1-=self.y1
            self.y2-=self.y2



rectangle_object1=rectangle(0,100,30,160)        # creating the 2 paddles/rectangles
rectangle_object2=rectangle(870,100,900,160)        # creating the 2 paddles/rectangles

# player-1 Movement variables/keys
apressed=False
wpressed=False

# main game loop
run = True
clock = pygame.time.Clock()
ball_object=ball()               # creating  the ball
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                apressed = True
            if event.key == pygame.K_w:
                wpressed=True

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                apressed=False
            if event.key==pygame.K_w:
                wpressed=False


    if apressed==True:
        rectangle_object1.downmovement()

    if wpressed==True:
        rectangle_object1.upmovement()

    #  --------key listner method-2---------

    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_a]:
    #     print("a")
    #     rectangle_object.downmovement()
    #
    # elif pressed[pygame.K_w]:
    #     print("w")
        # rectangle_object.upmovement()


    window.fill(color="red")
    # creating and calling methods for ball

    ball_object.draw();
    ball_object.move()
    ball_object.boundarycollision()

    # creating and calling methods for rectangle/paddle

    rectangle_object1.drawrect()
    rectangle_object2.drawrect()

    pygame.display.update()

pygame.quit()

