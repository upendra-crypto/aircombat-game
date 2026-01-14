from turtle import *
import random
class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1.5,stretch_len=1.5)
        self.color("yellow")
        self.penup()
        self.goto(random.randint(-360,360),330)
        self.setheading(270)
        self.speed(0)
    def move(self):
        self.fd(5)