from turtle import Turtle
import time





UP = 90
DOWN = 270



class Paddle:
    def __init__(self, position):
        self.position = self.create_paddle(position)



    def create_paddle(self, position):
        paddle = Turtle('square')
        paddle.speed('fastest')
        paddle.turtlesize(1, 6)
        paddle.seth(UP)
        paddle.penup()
        paddle.goto(position)
        paddle.color('white')
        return paddle

    def move_up(self):
        if self.position.ycor() < 240:
            self.position.seth(UP)
            self.position.forward(20)

    def move_down(self):
        if self.position.ycor() > -240:
            self.position.seth(DOWN)
            self.position.forward(20)








