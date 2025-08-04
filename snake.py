from turtle import Turtle, Screen


s = Screen()
s.screensize(600,600)

up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.lst = []
        self.create_snake()
        self.game_over = True
        self.first = self.lst[0]

    def le(self):
        if self.first.heading() != right:
            self.first.setheading(left)

    def r(self):
        if self.first.heading() != left:
            self.first.setheading(right)

    def u(self):
        if self.first.heading() != down:
            self.first.setheading(up)

    def d(self):
        if self.first.heading() != up:
            self.first.setheading(down)

    def create_snake(self, g = 2):
        n = 0
        for i in range(g):
            t = Turtle(shape="square")
            t.penup()
            t.goto(n, 0)
            t.color("black")
            self.lst.append(t)
            n -= 20


    def move(self):
        for i in range(len(self.lst) - 1, 0, -1):
            x = self.lst[i - 1].xcor()
            y = self.lst[i - 1].ycor()
            self.lst[i].goto(x, y)
        self.first.forward(20)

    def extra(self):
        last_segment = self.lst[-1]
        t = Turtle(shape="square")
        t.penup()
        t.color("black")
        t.goto(last_segment.xcor(), last_segment.ycor())
        self.lst.append(t)

    def re(self):
        self.lst = []
        self.create_snake()