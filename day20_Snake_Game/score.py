from turtle import Turtle
import  sys

ALIGN= 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.highest_score = 0
        self.read_file()

        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.points} High Score: {self.highest_score} ', align=ALIGN, font=FONT)


    def reset(self):
        if self.points > self.highest_score:
            self.highest_score = self.points
            self.write_score()

        self.points = 0
        self.update_scoreboard()

    def write_score(self):
        with open('score.txt', 'w') as file:
            file.write(str(self.highest_score))

    def read_file(self):
        try:
            with open('score.txt') as file:
                score = int(file.read())
                self.highest_score = score

        except AttributeError:
            print('error')

    def increment_points(self):
        self.points += 1
        self.update_scoreboard()

    """def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGN, font=FONT)"""



