from turtle import Turtle
from food import Food

ALLIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        # self.increment()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", False, ALLIGNMENT, FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", False, ALLIGNMENT, FONT)


    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()