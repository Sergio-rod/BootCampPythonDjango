from turtle import Turtle
import time


def create_snake():
    snake_dots = []
    for _ in range(3):
        new_dot = Turtle()
        new_dot.color('white')
        new_dot.shape('square')
        new_dot.penup()
        snake_dots.append(new_dot)
    return snake_dots


# Set snake position
def initial_position(snake_dots):
    snake = []
    x_cor = 0
    for dot in snake_dots:
        dot.setx(x_cor)
        snake.append(dot)
        x_cor -= 20
    return snake


def move_snake(snake):
    time.sleep(.1)
    for snake_dot in range(len(snake) - 1, 0, -1):
        new_x = snake[snake_dot - 1].xcor()
        new_y = snake[snake_dot - 1].ycor()
        snake[snake_dot].goto(new_x, new_y)
    snake[0].forward(20)
    snake[0].left(90)
