from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')

# Creating Snake

snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'a')


game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    # Detect colition with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_points()
    # Dtect colition with corners
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()



screen.exitonclick()
