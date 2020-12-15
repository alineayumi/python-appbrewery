from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.show_score()

    def update_score(self, score):
        self.level = score
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
