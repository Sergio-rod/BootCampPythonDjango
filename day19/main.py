from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Choice your turtle", prompt="Select the color that you think will win")


colors = ['green', 'blue', 'gray', 'black']
y_cor = 150
all_turtles = []
for i in range(4):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(-200, y=y_cor)
    new_turtle.color(colors[i])

    all_turtles.append(new_turtle)
    y_cor -= 100

if user_choice:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 230:
            print("the winner is ", i.pencolor())
            if user_choice != i.pencolor():
                print('Looser')
                exit()
            else:
                print('Winner')
                exit()
        else:

            rand_distance = random.randint(0, 10)
            i.forward(rand_distance)

screen.exitonclick()
