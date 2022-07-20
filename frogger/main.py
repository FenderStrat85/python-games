from re import M
from turtle import Screen
from frog import Frog
from motorbike import Motorbike
from car import Car
from lorry import Lorry
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=1200)
screen.bgcolor('gray')
screen.title('Frogger')
screen.tracer(0)

game_is_on = True

frog = Frog()
scoreboard = Scoreboard()
scoreboard.update_score()

motorbikes =[]
motorbike_starting_positions =[(-400, -200), (-200, -200), (0, -200), (200, -200), (400, -200)]
for pos in motorbike_starting_positions:
  motorbike = Motorbike(pos)
  motorbikes.append(motorbike)

cars = []
car_starting_positions = [(-300, 0), (0, 0), (300, 0), (600, 0)]
for pos in car_starting_positions:
  car = Car(pos)
  cars.append(car)

lorries = []
lorry_starting_positions = [(-700, 200),(-400, 200), (-100, 200), (200, 200)]
for pos in lorry_starting_positions:
  lorry = Lorry(pos)
  lorries.append(lorry)

screen.listen()
screen.onkey(frog.go_forward, 'Up')
screen.onkey(frog.go_backward, 'Down')
screen.onkey(frog.go_left, 'Left')
screen.onkey(frog.go_right, 'Right')

while game_is_on:
  time.sleep(0.1)
  screen.update()
  for item in motorbikes:
    item.move_forward()
    if item.xcor() > 400:
      item.goto(-400, -200) 
    if frog.distance(item) <= 5:
      scoreboard.frog_dies()
      scoreboard.update_score()
      frog.restart()

  
  for item in cars:
    item.move_backward()
    if item.xcor() < -600:
      item.goto(500, 0)
    if frog.distance(item) <= 5:
      scoreboard.frog_dies()
      scoreboard.update_score()
      frog.restart()
  
  for item in lorries:
    item.move_forward()
    if item.xcor() > 500:
      item.goto(-700, 200) 
    if frog.distance(item) <= 5:
      scoreboard.frog_dies()
      scoreboard.update_score()
      frog.restart()
  
  if frog.ycor() > 350:
    scoreboard.frog_lives()
    scoreboard.update_score()
    frog.restart()


screen.exitonclick()