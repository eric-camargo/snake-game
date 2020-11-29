from turtle import Turtle

ACCELERATION_RATE = 0.03
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.tail = self.snake_body[-1]
        self.speed = 0.1

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.extend(position)
        self.head = self.snake_body[0]

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()

    def move(self):
        for seg_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_number - 1].xcor()
            new_y = self.snake_body[seg_number - 1].ycor()
            self.snake_body[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def extend(self, position):
        bod = Turtle("square")
        bod.penup()
        bod.color("white")
        bod.goto(position)
        self.snake_body.append(bod)


    def grow(self):
        self.extend(self.snake_body[-1].position())
        self.speed_up()


    def speed_up(self):
        self.speed = self.speed * (1 - ACCELERATION_RATE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)