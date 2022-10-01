from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        random_point_x = random.randint(-270, 270)
        random_point_y = random.randint(-270, 270)
        self.goto(random_point_x, random_point_y)

