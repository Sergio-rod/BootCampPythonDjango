import time
from turtle import Screen, Turtle
from paddle import Paddle
from score import ScoreBoard
from ball import Ball

POSITIONS1 = [(-280, 40), (-280, 20), (-280, 0), (-280, -20), (-280, -40)]
POSITIONS2 = [(280, 40), (280, 20), (280, 0), (280, -20), (280, -40)]





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


paddle = Paddle(POSITIONS1)
paddle1 = Paddle(POSITIONS2)
score = ScoreBoard()
ball = Ball()


# paddle 2



screen.listen()
screen.onkeypress(paddle.move_up, 'w')
screen.onkeypress(paddle.move_down, 's')






game_on = True
banner = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()







    if banner:
        paddle1.move_up()
        if not(paddle1.highest_segment.ycor() < 280):
            banner = False
    elif not banner:
        paddle1.move_down()
        if not(paddle1.lowest_segment.ycor() > -280):
            banner = True

    # Detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # Detect colision with left paddle
    for segment in paddle.segments:
        if ball.distance(segment) < 30:
            ball.bounce_x()
            score.increment_left_score()

    # Detect colision with right paddle
    for segment in paddle1.segments:
        if ball.distance(segment) < 30:
            ball.bounce_x()
            score.increment_right_score()








screen.exitonclick()




