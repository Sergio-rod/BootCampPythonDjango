from turtle import Screen, Turtle
from paddle import Paddle
from score import ScoreBoard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)


# CREATE BOARD

startPosition = 280
for i in range(0,30,2):
    # CREATE BOARD
    dot_line = Turtle('square')
    dot_line.turtlesize(stretch_len=.2)
    dot_line.color('white')
    dot_line.speed('fastest')
    dot_line.penup()
    dot_line.goto(0, startPosition)
    startPosition -= 40


# ---------


player1 = Paddle()
score = ScoreBoard()







screen.listen()
screen.onkeypress(player1.move_up, 'w')
screen.onkeypress(player1.move_down, 's')



game_on = True

while game_on:
    screen.update()






screen.exitonclick()