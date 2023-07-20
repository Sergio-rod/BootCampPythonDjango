from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    randomize_color = (r, g, b)
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
    sergio_turtle.forward(distance)
    sergio_turtle.setheading(angle)


for i in range(300):
    random_walk(movements)


screen = Screen()
screen.exitonclick()
