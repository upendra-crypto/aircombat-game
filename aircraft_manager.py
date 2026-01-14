from turtle import Turtle

class AirCraft(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("arrow")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        self.speed(0)

    def l_move(self):
        if self.xcor() > -360:
            self.goto(self.xcor() - 20, self.ycor())

    def r_move(self):
        if self.xcor() < 360:
            self.goto(self.xcor() + 20, self.ycor())
