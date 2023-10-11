import pygame
import random
pygame.init()
width=800
height=600
window=pygame.display.set_mode((width,height))           #  setting the window to appear on the screen
pygame.display.set_caption("first pygame")               # set the title of window


color="#3efa7a"
fps=60
# main function

# coordinates of the circle

class circle():
    def __init__(self):
        self.xpos = random.randint(0, 800)
        self.ypos = random.randint(0, 600)
        self.radius = random.randint(20, 60)
        self.xspeed = random.randint(-5, 5)
        self.yspeed = random.randint(-5, 5)

    def draw(self):
        window.fill(color)
        pygame.draw.circle(window, center=(self.xpos, self.ypos), radius=self.radius, color="blue")

    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed

    def boundary_collision(self):
        if (self.xpos + self.radius > width) or (self.xpos - self.radius < 0):
            self.xspeed = -self.xspeed

        if (self.ypos + self.radius > height) or (self.ypos - self.radius < 0):
            self.yspeed = -self.yspeed


circle_obj1=circle()
circle_obj2=circle()
print(f"circle_obj: xpos={circle_obj1.xpos}, ypos={circle_obj1.ypos}")
print(f"circle_obj2: xpos={circle_obj2.xpos}, ypos={circle_obj2.ypos}")

clock=pygame.time.Clock()
run=True
while run:                                          # to appear the window on the screen
    clock.tick(fps)
    for event in pygame.event.get():                # get the event
        if event.type==pygame.QUIT:                 # if user presses the close button on the window =>close the window
            run=False
    circle_obj1.draw()
    circle_obj1.move()
    circle_obj1.boundary_collision()

    circle_obj2.draw()
    circle_obj2.move()
    circle_obj2.boundary_collision()
    pygame.display.update()



pygame.quit()



