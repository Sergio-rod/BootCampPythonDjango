from turtle import Turtle, Screen

"""
sergio_turtle = Turtle()

sergio_turtle.shape('turtle')
sergio_turtle.color('red')

for i in range(4):
   for j in range(6):
    sergio_turtle.forward(20)
    sergio_turtle.penup()
    sergio_turtle.forward(20)
    sergio_turtle.pendown()

   sergio_turtle.right(90)
"""

sergio_turtle = Turtle()

sergio_turtle.shape('turtle')
sergio_turtle.color('red')


for i in range(3, 11):
    for j in range(i):
        current_degrees = 360/i
        sergio_turtle.forward(50)
        sergio_turtle.left(current_degrees)


















screen = Screen()
screen.exitonclick()
