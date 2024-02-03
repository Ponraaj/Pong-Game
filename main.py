from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import  time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.update()

ball = Ball()
while True:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 328 or ball.distance(l_paddle) < 50 and ball.xcor() < -328:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()