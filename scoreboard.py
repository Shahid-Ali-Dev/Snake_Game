from turtle import Turtle
Font = ("Courier",24,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        self.hsc = 0

    def display(self):
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color("black")
        self.write(f"Score: {self.sc} High Score: {self.hsc}",False, align="center",font= Font)

    def score(self):
        self.sc += 1

    def reset(self):
        if self.sc > self.hsc:
            self.sc = self.hsc

    def over(self):
        self.goto(0,0)
        self.write(f"Sorry your Snake died.",False, align="center",font= Font)