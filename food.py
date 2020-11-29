from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = 20*random.randint(-14, 14)
        random_y = 20*random.randint(-14, 14)
        new_position = (random_x, random_y)
        self.goto(new_position)
