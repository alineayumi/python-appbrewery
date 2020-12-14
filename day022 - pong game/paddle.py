from turtle import Turtle
RIGHT = 350
LEFT = -350


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        if side == "right":
            self.x_pos = RIGHT
        elif side == "left":
            self.x_pos = LEFT
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(x=self.x_pos, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
