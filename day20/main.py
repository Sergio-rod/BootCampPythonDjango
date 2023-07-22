from turtle import Screen
from snake import move_snake, create_snake, initial_position

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')

# Creating Snake
segments = create_snake()

snake = initial_position(segments)

game_is_on = True
while game_is_on:
    screen.update()
    move_snake(snake)


screen.exitonclick()
