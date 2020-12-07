# import colorgram
#
# colors = colorgram.extract('image.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()


color_list = [(232, 226, 213), (218, 218, 223), (108, 110, 127), (213, 154, 94), (140, 141, 152), (227, 214, 104), (195, 60, 24), (233, 216, 225), (224, 234, 226), (181, 159, 38)]

pos_x = -250
pos_y = -315
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

for y in range(10):
    pos_x = -325
    for x in range(10):
        tim.setposition(pos_x, pos_y)
        tim.dot(20, random.choice(color_list))
        pos_x += 70
    pos_y += 70

screen = t.Screen()
screen.exitonclick()
