from turtle import Turtle
import time


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_dots(self):
        snake_dots = []
        for _ in range(3):
            new_dot = Turtle()
            new_dot.color('white')
            new_dot.shape('square')
            new_dot.penup()
            snake_dots.append(new_dot)
        return snake_dots

    def create_snake(self):
        snake_dots = self.create_dots()
        x_cor = 0
        for dot in snake_dots:
            dot.setx(x_cor)
            self.snake.append(dot)
            x_cor -= 20

    def move(self):
        time.sleep(.1)
        for snake_dot in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_dot - 1].xcor()
            new_y = self.snake[snake_dot - 1].ycor()
            self.snake[snake_dot].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        self.snake[0].seth(90)

    def down(self):
        self.snake[0].seth(270)

    def right(self):
        self.snake[0].seth(0)

    def left(self):
        self.snake[0].seth(180)

