from turtle import Turtle
import time

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

STARTING_POSITIONS = ((0,0),(-20,0),(-40,0))


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.speed = .1

    def add_dot(self, position):
        new_dot = Turtle('square')
        new_dot.color('green')
        new_dot.penup()
        new_dot.goto(position)
        self.snake.append(new_dot)

    def extend(self):
        self.add_dot(self.snake[-1].position())
        self.speed *= .98
        print(self.speed)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_dot(position)
    def reset(self):

        for seg in self.snake:
            seg.goto(1000, 1000)

        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.speed = .1


    def move(self):
        time.sleep(self.speed)
        for snake_dot in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_dot - 1].xcor()
            new_y = self.snake[snake_dot - 1].ycor()
            self.snake[snake_dot].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

