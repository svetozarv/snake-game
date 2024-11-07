from turtle import Turtle

COLOR = "green"
STARTING_POSITIONS = [
    (0, 0),
    (0, -20),
    (0, -40)
]

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)


    def add_segment(self, position): # TODO
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color(COLOR)
        turtle.goto(position)
        self.segments.append(turtle)
        return turtle


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
