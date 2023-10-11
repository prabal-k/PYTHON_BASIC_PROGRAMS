import tkinter as tk
import math

class BresenhamCanvas(tk.Canvas):
    def draw_point(self, x, y, color="red"):
        self.create_line(x, y, x + 1, y + 1, fill=color)

    def draw_circle_points(self, x, y, center_x, center_y, color="red"):
        self.draw_point(center_x + x, center_y + y, color)
        self.draw_point(center_x - x, center_y - y, color)
        self.draw_point(center_x + x, center_y - y, color)
        self.draw_point(center_x - x, center_y + y, color)

        if x != y:
            self.draw_point(center_x + y, center_y + x, color)
            self.draw_point(center_x - y, center_y - x, color)
            self.draw_point(center_x + y, center_y - x, color)
            self.draw_point(center_x - y, center_y + x, color)

    def draw_circle(self, center_x, center_y, radius, line_thickness, color="red"):
        x = 0
        yin = radius - int(line_thickness / 2)
        yout = radius + int(line_thickness / 2)
        din = 1 - radius - int(line_thickness / 2)
        deltaEin = 3
        deltaSEin = -2 * (radius - int(line_thickness / 2)) + 5
        dout = 1 - radius + int(line_thickness / 2)
        deltaEout = 3
        deltaSEout = -2 * (radius + int(line_thickness / 2)) + 5

        for y in range(yin, yout):
            self.draw_circle_points(x, y, center_x, center_y, color)

        while yout > x:
            if din < 0:
                din = din + deltaEin
                deltaEin = deltaEin + 2
                deltaSEin = deltaSEin + 2
            else:
                din = din + deltaSEin
                deltaEin = deltaEin + 2
                deltaSEin = deltaSEin + 4
                yin = yin - 1

            if dout < 0:
                dout = dout + deltaEout
                deltaEout = deltaEout + 2
                deltaSEout = deltaSEout + 2
            else:
                dout = dout + deltaSEout
                deltaEout = deltaEout + 2
                deltaSEout = deltaSEout + 4
                yout = yout - 1

            x = x + 1
            for y in range(yin, yout):
                self.draw_circle_points(x, y, center_x, center_y, color)

def run():
    CANVAS_SIZE = 600
    root = tk.Tk()
    canvas = BresenhamCanvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
    canvas.pack()
    margin = CANVAS_SIZE / 10
    origin_x = int(CANVAS_SIZE / 2)
    origin_y = int(CANVAS_SIZE / 2)
    center_dist = ((CANVAS_SIZE / 2) - 2 * margin)
    radius = margin * 2
    n_circles = 10
    angle_step = (2 * math.pi) / n_circles

    for i in range(n_circles):
        theta = angle_step * i
        center_x = int(center_dist * math.cos(theta)) + origin_x
        center_y = int(center_dist * math.sin(theta)) + origin_y
        canvas.create_oval(center_x, center_y, center_x+radius,center_y+radius, color="blue")

    root.mainloop()

if __name__ == "__main__":
    run()
