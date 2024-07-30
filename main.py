import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, " ")

game_is_on = True
distance = 5
cars = []
counter = 0
level = 1
frequency = 7

for x in range(15):
    x_cor = random.randint(-305, 305)
    car = CarManager(x_cor)
    cars.append(car)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if counter % frequency == 0:
        car = CarManager(310)
        cars.append(car)

    for car in cars:
        car.move(distance)

    for car in cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 300:
        player.reset()
        level += 1
        scoreboard.update_scoreboard(level)
        distance += 2
        if counter != 4:
            frequency -= 1

    counter += 1

screen.exitonclick()
