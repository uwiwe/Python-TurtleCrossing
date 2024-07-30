from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-260, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.write("Level: 1", align="left", font=("Times New Roman", 25, "normal"))

    def update_scoreboard(self, level):
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {level}", align="left", font=("Times New Roman", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 25, "normal"))
