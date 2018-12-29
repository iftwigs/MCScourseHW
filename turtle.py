import math
import turtle

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def distance_to_other(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y) 

point = Point(0, 0, "red")
other_point = Point(30, 40, "black")
print(point)
assert(point.distance_to_other(other_point) == 50)
print("Fine!")

class Drawer:

    def draw_rect(self, side):
        counter = 0
        while counter < 4:
        	turtle.fd(side)
        	turtle.left(90)
        	counter += 1
        
    def draw_triangle(self, side):
    	self.side = side
        counter = 0
        while counter < 3:
        	turtle.fd(side)
        	turtle.left(120)
        	counter += 1

    def draw_circle(self, radius):
        self.radius = radius
        turtle.circle(radius)

    def draw_point(self, point):
    	turtle.up()
    	turtle.goto(point.x, point.y)
    	turtle.down()
    	turtle.color(point.color)
    	self.draw_rect(1)

    def draw_points(self, points):
    	for point in points:
    		self.draw_point(point)

drawer = Drawer()
drawer.draw_rect(50)
drawer.draw_triangle(50)
drawer.draw_circle(50)
turtle.pensize(10)
drawer.draw_point(Point(100, 100, "purple"))
drawer.draw_points([Point(100, 100, "purple"), Point(-100, 50, "green")])




