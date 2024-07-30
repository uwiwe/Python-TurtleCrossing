from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randint(0, 5)])
        y_cor = random.randint(-230, 230)
        self.goto(x_cor, y_cor)

    def move(self, distance):
        self.forward(STARTING_MOVE_DISTANCE)
