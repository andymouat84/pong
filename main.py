import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
LEFT_PADDLE_POS = (-350, 0)
RIGHT_PADDLE_POS = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

left_paddle = Paddle(LEFT_PADDLE_POS)
right_paddle = Paddle(RIGHT_PADDLE_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if  ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
