from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width = 800, height = 800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
game_is_on = True

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()
  if ball.ycor() > 380 or ball.ycor() < -380:
    ball.bounce()

  if ball.distance(r_paddle) < 50 and ball.xcor() > 370:
    print('hit paddle')
    ball.paddle_hit()

  if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
    scoreboard.left_scores()
    scoreboard.update_score()
    ball.goto(0,0)
  
  if ball.distance(l_paddle) < 50 and ball.xcor() < -370:
    ball.paddle_hit()

  if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
    scoreboard.right_scores()
    scoreboard.update_score()
    ball.goto(0,0)
  




screen.exitonclick()