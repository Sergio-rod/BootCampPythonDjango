from turtle import Turtle

ALIGN= 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.points}', align=ALIGN, font=FONT)

    def increment_points(self):
        self.clear()
        self.points += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGN, font=FONT)



