from turtle import Screen
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')

# Creating Snake

snake = Snake()


screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'a')



game_is_on = True
while game_is_on:
    screen.update()
    snake.move()


screen.exitonclick()
