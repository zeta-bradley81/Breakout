from turtle import Turtle
from random import randint

# TODO I think i can optimize this with another function to nest in the paddle hit

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color(255, 255, 255)
        self.penup()
        self.spin_max = 10
        self.spin = 0
        self.x_move = 0
        self.y_move = -10
        self.x_direction = 'straight'

    # bouncing off a brick
    def brick_strike(self, where):
        if where == 'side':
            self.x_move *= -1
        else:
            self.x_move *= -1
            self.y_move *= -1
        self.spin_regulation()

    # bouncing off the top
    def ceiling_bounce(self):
        self.y_move += 1
        self.y_move *= -1
        if self.x_move == 0:
            self.x_move -= 1

    def move(self):
        # print(self.x_move, self.y_move)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bouncing off the paddle
    # Positive x_move value means ball is moving left-to-right
    def paddle_bounce(self, xd):
        if self.x_move > 0:
            self.x_direction = 'right'
        elif self.x_move == 0:
            self.x_direction = 'straight'
        elif self.x_move < 0:
            self.x_direction = 'left'

        # Y always changes direction on a paddle bounce
        self.y_move *= -1

        # X changes direction depending on different things
        if self.x_direction == 'right':
            if xd > -35:
                self.x_move += -1
        else:
            if xd < 35:
                self.x_move *= -1

        # Setting the spin rates
        if -20 <= xd <= 20:
            # print(xd)
            self.spin += randint(-1, 1)
            self.spin_regulation()
            self.x_move += self.spin
            # print(f"xd={xd} x={self.x_move}, y={self.y_move}, spin={self.spin}, total={self.x_move + self.y_move}")

        elif -35 > xd > -20:
            # si = randint(0, 1)
            si = randint(1,2)
            if self.x_direction == 'right':
                self.spin += si
                self.spin_regulation()
                self.x_move += self.spin
            else:
                self.spin -= si
                self.spin_regulation()
                self.x_move += self.spin

        elif 20 < xd < 35:
            # si = 2
            si = randint(2,3)
            if self.x_direction == 'right':
                self.spin -= si
                self.spin_regulation()
                self.x_move += self.spin
            else:
                self.spin += si
                self.spin_regulation()
                self.x_move += self.spin

        elif xd <= -35:
            si = randint(3,4)
            # si = 3
            if self.x_direction == 'right':
                self.spin += si
                self.spin_regulation()
                self.x_move += self.spin
            else:
                self.spin -= si
                self.spin_regulation()
                self.x_move += self.spin

        elif xd >= 35:
            si = randint(5,6)
            # si = 4
            if self.x_direction == 'right':
                self.spin -= si
                self.spin_regulation()
                self.x_move += self.spin
            else:
                self.spin += si
                self.spin_regulation()
                self.x_move += self.spin

        self.spin *= -1
        if abs(self.spin) > 6:
            if randint(0,1) == 0:
                self.x_move *= -1

    def reset_ball(self):
        self.spin = 0
        # self.x_move = 0
        # self.y_move = -10
        self.x_direction = 'straight'
        self.hideturtle()
        self.x_move = 0
        self.y_move = 0
        self.goto(0, 0)
        self.showturtle()

    def spin_regulation(self):
        if abs(self.spin) > self.spin_max:
            if self.spin >= 0:
                self.spin = self.spin_max
            else:
                self.spin = -1 * self.spin_max

        if abs(self.y_move) < 5:
            if self.y_move >= 0:
                self.y_move = 5
            else:
                self.y_move = -5
        # print(f"{self.spin} = spin, xy={self.x_move},{self.y_move}" )

    # bouncing off the sides of the screen
    def wall_bounce(self):
        self.x_move *= -1
        if self.y_move > 0:
            self.y_move -= 1
        else:
            self.y_move += 1






