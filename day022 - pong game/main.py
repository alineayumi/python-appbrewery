from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreball import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

paddle_r = Paddle("right")
paddle_l = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # detect collision with paddle
    if (ball.xcor() >= 320 or ball.xcor() <= -320) and (ball.distance(paddle_r) <= 50 or ball.distance(paddle_l) <= 50):
        ball.bounce_x()

    # detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.left_point()
    elif ball.xcor() < -380:
        ball.restart()
        scoreboard.right_point()
    screen.update()


screen.exitonclick()
