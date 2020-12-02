# import turtle
#
# # Classes
# timmy = turtle.Turtle()
# print(timmy)
#
# # Attributes
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
#
# # Methods
# timmy.shape("turtle")
# timmy.color("chocolate")
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"
print(table)

