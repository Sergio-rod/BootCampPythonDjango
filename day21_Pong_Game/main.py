from turtle import Screen
from  paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)

player1 = Paddle()


screen.listen()
screen.onkey(player1.move_up, 'w')
screen.onkey(player1.move_down, 's')



screen.exitonclick()