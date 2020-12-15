from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CREATION_INTERVAL = 6


class CarManager:
    def __init__(self):
        self.cars = []
        self.i = 1

    def create_car(self):
        if self.i % CAR_CREATION_INTERVAL == 0:
            self.cars.append(Car())
        self.i += 1

    def move_cars(self, level):
        move_distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1)
        for car in self.cars:
            car.move(move_distance)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x=300, y=random.choice(range(-250, 250)))

    def move(self, move_distance):
        new_x = self.xcor() - move_distance
        self.goto(new_x, self.ycor())

    def delete(self):
        self.clear()