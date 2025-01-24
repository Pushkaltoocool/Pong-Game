from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_1position = (350, 0)
paddle_2position = (-350, 0)

paddle = Paddle(position=paddle_1position)
paddle2 = Paddle(position=paddle_2position)
ball = Ball(position=(0, 0))
scoreboard1 = Scoreboard(position=(250, 200))
scoreboard2 = Scoreboard(position=(-250, 200))


screen.listen()


screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")

game_is_on = True

while game_is_on:


    screen.update()

    scoreboard1.update_score()
    scoreboard2.update_score()
    ball.move()
    time.sleep(0.05)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 335 and ball.distance(paddle.paddle) < 50 or ball.xcor() < -335 and ball.distance(paddle2.paddle) < 50:
        ball.bounce1()

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce1()
        scoreboard1.score += 1
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce1()
        scoreboard2.score += 1

    if scoreboard1.score == 5:
        scoreboard1.update_score()
        winner = "Player 1"
        game_is_on = False
        scoreboard1.game_over(winner=winner)

    elif scoreboard2.score == 5:
        scoreboard2.update_score()
        winner = "Player 2"
        game_is_on = False
        scoreboard2.game_over(winner=winner)


screen.exitonclick()