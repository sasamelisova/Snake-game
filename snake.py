from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
screen = Screen()
screen.listen()
tim = Turtle()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.positions = []
        self.create_snake()
        self.head = self.positions[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.positions.append(tim)

    def reset(self):
        for position in self.positions:
            position.goto(1000, 1000)
        self.positions.clear()
        self.create_snake()
        self.head = self.positions[0]

    def extend(self):
        self.add_segment(self.positions[-1].position())

    def move(self):
        for seg_num in range(len(self.positions) - 1, 0, -1):
            new_x = self.positions[seg_num - 1].xcor()
            new_y = self.positions[seg_num - 1].ycor()
            self.positions[seg_num].goto(new_x, new_y)
        self.positions[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)






