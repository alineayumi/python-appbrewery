import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
angles = [0, 90, 180, 270]

tim.pensize(10)
tim.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g , b)
    return color


def random_walk():
    red = random.randint(0, 255)
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(angles))


for _ in range(200):
    random_walk()