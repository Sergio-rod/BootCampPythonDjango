from turtle import  Turtle


POSITIONS1 = [(-280, 40), (-280, 20), (-280, 0), (-280, -20), (-280, -40)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.highest_segment = self.segments[0]
        self.lowest_segment = self.segments[len(self.segments)-1]

    def create_paddle(self):
        for position in POSITIONS1:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_up(self):
        self.highest_segment.seth(UP)
        for segment in range(len(self.segments)-1, 0, -1):
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(-280, new_y)
        self.highest_segment.forward(20)

    def move_down(self):
        self.lowest_segment.seth(DOWN)
        for segment in range(0, len(self.segments)-1):
            new_y = self.segments[segment + 1].ycor()
            self.segments[segment].goto(-280, new_y)
        self.lowest_segment.forward(20)




