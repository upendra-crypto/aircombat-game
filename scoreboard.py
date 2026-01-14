from turtle import *
import winsound
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score=0
        self.high=0
        self.get_high_score()
        self.update_score()
    def get_high_score(self):
        fp=open("high_score.txt","r")
        self.high=int(fp.read())
        fp.close()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score={self.high}", align="center", font=("Impact", 20, "normal"))
    def increase_score(self):
        self.score += 1
        self.update_score()
    def check(self):
        if self.high < self.score:
            fp=open("high_score.txt","w")
            fp.write(str(self.score))
            fp.close()
    def game_over(self):
        winsound.Beep(1000,150)
        self.goto(0,0)
        self.check()
        self.write("GAME OVER",align="center",font=("Impact", 100, "normal"))