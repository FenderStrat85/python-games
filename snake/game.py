from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My snake game! ')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

top_limit = 300
bottom_limit = -300
left_limit = -300
right_limit = 300

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    scoreboard.update_scoreboard()
    snake.add_piece()

  if snake.head.xcor() > right_limit or snake.head.xcor() < left_limit:
    scoreboard.game_reset()
    snake.reset()
  
  if snake.head.ycor() > top_limit or snake.head.ycor() < bottom_limit:
    scoreboard.game_reset()
    snake.reset()
  
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.game_resest()
      snake.reset()

screen.exitonclick()