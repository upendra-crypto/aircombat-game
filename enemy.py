from turtle import Turtle
import random

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)


        self.shape("triangle")
        self.color("orange")
        self.shapesize(stretch_wid=2.2, stretch_len=2.2)


        self.setheading(270)


        self.goto(random.randint(-360, 360), 330)

    def move(self):
        self.forward(5)
