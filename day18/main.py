from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    randomize_color = (r / 255.0, g / 255.0, b / 255.0)  # Normalize to the range [0.0, 1.0]
    return randomize_color


sergio_turtle = Turtle()

sergio_turtle.shape('turtle')

sergio_turtle.speed('fastest')
sergio_turtle.pensize(12)

movements = [0, 90, 180, 270, 360]
"""colors = [
    "red", "orange", "yellow", "green", "blue", "purple",
    "cyan", "magenta", "brown", "gray", "black", "white"
]"""


def random_walk(angle):

    angle = random.choice(angle)
    distance = 30
    sergio_turtle.color(random_color())
    sergio_turtle.back(distance)
    sergio_turtle.setheading(angle)


for i in range(100):
    random_walk(movements)


screen = Screen()
screen.exitonclick()
