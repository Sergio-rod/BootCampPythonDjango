import time
from turtle import Screen, Turtle
from paddle import Paddle
from score import ScoreBoard
from ball import Ball

POSITION1 = (-280, 0)
POSITION2 = (280, 0)





screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)


# CREATE BOARD

startPosition = 280
for i in range(0, 30 ,2):
    # CREATE BOARD
    dot_line = Turtle('square')
    dot_line.turtlesize(stretch_len=.2)
    dot_line.color('white')
    dot_line.speed('fastest')
    dot_line.penup()
    dot_line.goto(0, startPosition)
    startPosition -= 40


# ---------


paddle = Paddle(POSITION1)
paddle1 = Paddle(POSITION2)
score = ScoreBoard()
ball = Ball()


# paddle 2



screen.listen()

screen.onkeypress(paddle.move_up, 'w')
screen.onkeypress(paddle.move_down, 's')

"""
screen.onkeypress(paddle1.move_up, '-')
screen.onkeypress(paddle1.move_down, '+')
"""






game_on = True
banner = True

while game_on:
    time.sleep(.1)
    screen.update()
    ball.move()


    # AutomaticPlay
    if banner:
        paddle1.move_up()
        if not(paddle1.position.ycor() < 240):
            banner = False
    elif not banner:
        paddle1.move_down()
        if not(paddle1.position.ycor() > -240):
            banner = True

    # Detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect colision with left paddle

    if ball.distance(paddle.position) < 30:
        ball.bounce_x()
        score.increment_left_score()

    # Detect colision with right paddle
    if ball.distance(paddle1.position) < 30:
        ball.bounce_x()
        score.increment_right_score()

    # Detect right miss
    if ball.xcor() > 280:
        ball.reset_position()
        # Detect right miss
    if ball.xcor() < -280:
        ball.reset_position()








screen.exitonclick()




