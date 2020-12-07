import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colors = [
    "bisque",
    "light salmon",
    "tomato",
    "red",
    "crimson",
    "dark salmon",
    "salmon",
    "indian red",
]


def draw_polygon(sides, polygon_size):
    angle = 360 / sides
    tim.color(random.choice(colors))
    for _ in range(sides):
        tim.forward(polygon_size)
        tim.right(angle)


size = 100

for _ in range(3, 11):
    draw_polygon(_, size)
