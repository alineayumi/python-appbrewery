from turtle import Turtle
RIGHT = 1
LEFT = -1
UP = 1
DOWN = -1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(x=0, y=0)
        self.x_dir = RIGHT
        self.y_dir = UP
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + 10 * self.x_dir
        new_y = self.ycor() + 10 * self.y_dir
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
