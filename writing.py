import time
from turtle import Turtle
FONT = 'Andale Mono'


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

    def game_over(self, h, w, score):
        self.goto(-(w/2)+w/13,0)
        thislist = ["G","A","M","E"," ", "O","V","E","R"]
        # self.write(arg="GAME OVER", font=(FONT, 100, 'normal'), align='center')

        for x in range(0,len(thislist)):
            self.write(arg=thislist[x], font=(FONT, 100, 'normal'), align='center')
            self.forward(100)
            time.sleep(0.5)

        self.goto(0, -250)
        self.write(arg=f"Score: {score}", font=(FONT, 24, 'normal'), align='center')

        self.goto(0, -350)
        self.write(arg='Hit "c" to continue', font=(FONT, 18, 'normal'), align='center')


    def levels(self, n=0):
        if n == 0:
            self.goto(0, 250)
            self.write(arg='Welcome to Break-anoid!', font=(FONT, 36, 'normal'), align='center')
            self.goto(0, 0)
            self.write(
                arg="Left Arrow: move left.\n\nRight Arrow: move right.\n\nUp Arrow: double-move left\n\nDown Arrow: double-move right",
                font=(FONT, 24, 'normal'), align='center')
            time.sleep(5)
            self.clear()
            self.levels(n=1)
        else:
            self.goto(0,0)
            self.write(arg=f"Level {n}",font=(FONT, 60, 'normal'), align='center')
            time.sleep(3)
            self.clear()

    def launch_instructions(self, top_y, row_height):
        self.goto(0,top_y-20*row_height)
        self.write(arg="Move paddle to target ball.\nClick space bar to launch.", font=(FONT, 24, 'normal'),align='center' )

    def congratulations(self, score=666):
        self.goto(0, 250)
        self.write(arg="Congratulations", font=(FONT, 48, 'normal'), align='center')
        self.goto(0, -250)
        self.write(arg=f"Score: {score}", font=(FONT, 24, 'normal'), align='center')
