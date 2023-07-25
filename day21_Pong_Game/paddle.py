from turtle import  Turtle
import time


POSITIONS1 = [(-280, 40), (-280, 20), (-280, 0), (-280, -20), (-280, -40)]
POSITIONS2 = [(280, 40), (280, 20), (280, 0), (280, -20), (280, -40)]


UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Paddle:
    def __init__(self):
        self.segments = []
        self.segments_1 = []
        self.create_paddle(self.segments, POSITIONS1)
        self.create_paddle(self.segments_1, POSITIONS2)
        self.highest_segment = self.segments[0]
        self.lowest_segment = self.segments[len(self.segments)-1]

    def create_paddle(self,segments, positions):
        for position in positions:
            new_segment = Turtle('square')
            new_segment.speed('fastest')
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color('white')
            segments.append(new_segment)


    def move_up(self):
        self.highest_segment.seth(UP)
        for segment in range(len(self.segments)-1, 0, -1):
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].sety(new_y)
        self.highest_segment.forward(20)

    def move_down(self):
        self.lowest_segment.seth(DOWN)
        for segment in range(0, len(self.segments)-1):
            new_y = self.segments[segment + 1].ycor()
            self.segments[segment].sety(new_y)
        self.lowest_segment.forward(20)





