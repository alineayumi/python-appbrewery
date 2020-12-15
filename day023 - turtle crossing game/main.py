import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle = Player()
level = 1
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars(level)
    # detect when player hits the top edge
    if turtle.ycor() > 280:
        turtle.reset_position()
        level += 1
        score.update_score(level)
    # detect when player collides with a car
    for car in car_manager.cars:
        if turtle.distance(car) <= 25:
            score.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()
