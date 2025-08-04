from turtle import Turtle, Screen
s = Screen()
s.register_shape("spinning-poop.gif")
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("spinning-poop.gif")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")


    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
