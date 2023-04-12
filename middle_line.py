from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=60, stretch_len=0.1)
        self.penup()
        self.goto(0, 300)


