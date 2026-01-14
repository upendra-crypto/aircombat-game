from turtle import *
class Bullets(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.goto(position)
        self.color("red")
        self.setheading(90)
        self.penup()
        self.speed(0)
    def move(self):
        self.fd(20)
