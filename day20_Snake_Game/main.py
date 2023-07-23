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

    # Detect coalition with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment_points()
    # Detect coalition with corners
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    # Detect coalition with itself
    for dot in snake.snake[1:]:
        if snake.head.distance(dot) < 10:
            game_is_on = False
            score.game_over()





screen.exitonclick()
