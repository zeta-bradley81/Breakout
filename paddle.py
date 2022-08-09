"""
Takes the screen dimensions as an arguments
"""
from turtle import Turtle

MOVE_DISTANCE = 49

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.penup()
        self.resizemode('user')
        self.shapesize(1, 5)
        # self.color(0, 0, 0)
        self.color(178,34,52)
        self.goto(0, -int((y/2))+10)
        self.speed(8)
        self.dir = ""
        self.x = x

    def move_left(self):
        if -self.x/2 + 100 < self.xcor():
            self.backward(MOVE_DISTANCE)
            self.dir = 'b'

    def move_right(self):
        if self.x/2 -95 > self.xcor():
            self.forward(MOVE_DISTANCE)
            self.dir = 'f'

    def double_up(self):
        if -self.x/2 + 100 < self.xcor():
            self.backward(MOVE_DISTANCE * 2)

    def double_down(self):
        if self.x/2 -95 > self.xcor():
            self.forward(MOVE_DISTANCE * 2)









