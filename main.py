from time import sleep
from turtle import Screen
import tkinter as tk
import paddle
from writing import Message
from ball import Ball

from blocks import BlocksAndBoards

LIVES_STARTING = 3
lives_remaining = LIVES_STARTING
between_turns = False
starting_block_count = 0
writing = Message()
level = 1
score = 0

# TODO fix edge bug

# Setting up the window, using Tk to get the dimensions of the player's monitor
root = tk.Tk()
root.withdraw()
monitor_width = root.winfo_screenwidth()
monitor_height = root.winfo_screenheight()
screen_height = int(monitor_height)
screen_width = int(monitor_height * 1.25)

screen = Screen()
screen.colormode(255)
screen_color = 'black'
screen.bgcolor(screen_color)
screen.setup(width=screen_width, height=screen_height)
screen.title('Break-anoid: The Tribute')
# Turning off the tracer here allows the game to draw itself quickly. I turn it back on below.
screen.tracer(0)

# Setting up the dimensions for the blocks relative to the screen.
TURTLE_BASE_PIXELS = 20
BLOCKS_PER_ROW = int(15)
BLOCK_WIDTH = screen_width / BLOCKS_PER_ROW
BLOCK_WIDTH_FACTOR = BLOCK_WIDTH / TURTLE_BASE_PIXELS
BLOCK_HEIGHT_FACTOR = 1.5
BLOCK_HEIGHT = TURTLE_BASE_PIXELS * BLOCK_HEIGHT_FACTOR

#   These variables will be used to determine where to place the rows and columns of blocks
LEFT_X = (-screen.window_width() / 2) + (.5 * BLOCK_WIDTH)
TOP_Y = (screen.window_height() - (TURTLE_BASE_PIXELS * BLOCK_HEIGHT_FACTOR)) / 2
ROW_HEIGHT = TURTLE_BASE_PIXELS * BLOCK_HEIGHT_FACTOR

# variables for ball
bottom_limit = -(screen.window_height() / 2)
top_limit = screen.window_height() / 2 - .5 * ROW_HEIGHT
left_limit = -(screen.window_width() / 2) + 20
right_limit = screen.window_width() / 2 - 20

# Build the blocks
bnb = BlocksAndBoards(bhf=BLOCK_HEIGHT_FACTOR,
                      bpr=BLOCKS_PER_ROW,
                      bw=BLOCK_WIDTH,
                      bwf=BLOCK_WIDTH_FACTOR,
                      lx=LEFT_X,
                      rh=ROW_HEIGHT,
                      topy=TOP_Y)


def launch_ball():
    """ Hitting the space bar between turns re-starts the game."""
    global between_turns
    if between_turns:
        between_turns = False
        screen.update()
        ball.x_move = 0
        ball.y_move = -10
        ball.move()


def next_level(current_level):
    global block_count
    bnb.clear()
    ball.hideturtle()
    paddle.hideturtle()
    screen.update()
    writing.levels(n=current_level)
    if level == 2:
        block_count = bnb.level_2()
    elif level == 3:
        writing.congratulations(score)
    ball.showturtle()
    ball.y_move = -10
    paddle.showturtle()


def game_over():
    global game_on
    bnb.hide_blocks()
    ball.hideturtle()
    paddle.hideturtle()
    screen.update()
    writing.game_over(h=screen_height, w=screen_width, score=score)


def restart():
    global block_count, game_on, between_turns, lives_remaining, level, score
    if level == 2:
        block_count = bnb.level_2()
    else:
        block_count = bnb.level_1()
    bnb.show_blocks()
    ball.showturtle()
    ball.reset_ball()
    paddle.goto(0, -int(((monitor_height * .9) / 2)) + 10)
    paddle.showturtle()
    screen.update()
    game_on = True
    lives_remaining = 3
    score = 0
    ball.y_move = -10
    main_loop()


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
screen.update()

# Create the ball
ball = Ball()

# Create the paddle
paddle = paddle.Paddle(screen_width, monitor_height * .9)
paddle.color('blue')

# ~~~~~     Create the levels     ~~~~~
writing.levels()
block_count = bnb.level_1()

# Prepare to Play
paddle.showturtle()
screen.tracer(1)
screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')
screen.onkey(paddle.double_up, 'Up')
screen.onkey(paddle.double_down, 'Down')
screen.onkey(restart, "c")
screen.onkey(launch_ball, 'space')
screen.tracer(0)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

game_on = True


# Main Loop of the game
def main_loop():
    global between_turns, game_on, block_count, score, level, lives_remaining
    while game_on:
        sleep(0.01)
        screen.update()
        ball.move()

        if not between_turns:
            writing.clear()
        #  Sets the parameters for contact with the paddle
        if ball.ycor() < paddle.ycor() + 25 and \
                paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            ball.paddle_bounce((paddle.xcor() - ball.xcor()))

        # Sets the parameters for contact with the upper edge of the board
        if ball.ycor() > top_limit:
            ball.ceiling_bounce()

        # Sets the parameters to bound of the sides of the screen.
        if ball.xcor() < left_limit or ball.xcor() > right_limit:
            ball.wall_bounce()

        # These are the 'tunings' for hitting the blocks
        for r in range(0, 10):
            for c in range(0, BLOCKS_PER_ROW):
                i = bnb.block_dictionary[r][c]
                if ball.ycor() - .25 * BLOCK_HEIGHT < i.ycor() < ball.ycor() + .25 * BLOCK_HEIGHT \
                        and (ball.xcor() - .55 * BLOCK_WIDTH) < i.xcor() < (ball.xcor() + .55 * BLOCK_WIDTH):
                    i.goto(1000, 1000)
                    ball.brick_strike('side')
                    block_count -= 1
                    score += 1

                if ball.ycor() - .5 * BLOCK_HEIGHT < i.ycor() < ball.ycor() + .5 * BLOCK_HEIGHT \
                        and (ball.xcor() - .5 * BLOCK_WIDTH) < i.xcor() < (ball.xcor() + .5 * BLOCK_WIDTH):
                    i.goto(1000, 1000)
                    ball.brick_strike('front')
                    block_count -= 1
                    score += 1

                if block_count == 0:
                    score += 100
                    level += 1
                    next_level(level)

        # Sets the parameters for losing the ball
        if ball.ycor() < bottom_limit:
            lives_remaining -= 1
            paddle.goto(0, paddle.ycor())
            ball.reset_ball()
            if lives_remaining > 0:
                between_turns = True
            if lives_remaining == 0:
                game_on = False
                game_over()

        if between_turns:
            ball.goto(paddle.xcor(), 0)
            if lives_remaining == 2:
                writing.launch_instructions(TOP_Y, ROW_HEIGHT)


main_loop()
screen.exitonclick()
