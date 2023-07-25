from turtle import Turtle

ALIGN= 'center'
FONT = ('Arial', 40, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.left_score}\t{self.right_score}', align=ALIGN, font=FONT)

    def increment_right_score(self):
        self.clear()
        self.right_score += 1
        self.update_scoreboard()

    def increment_left_score(self):
        self.clear()
        self.left_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGN, font=FONT)


