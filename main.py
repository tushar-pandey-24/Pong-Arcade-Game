from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.collision()

    if ball.xcor() > 400:
        ball.refresh()
        score.l_point()

    if ball.xcor() < -410:
        ball.refresh()
        score.r_point()

    if score.l_score == 10 or score.r_score == 10:
        game_on = False

screen.exitonclick()
