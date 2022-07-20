
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('gray')

player = Player()
scoreboard = Scoreboard()
scoreboard.update_score()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_forward, 'Up')
screen.onkey(player.go_backward, 'Down')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on=False
            scoreboard.game_over()

    if player.ycor() > 270:
        player.level_complete()
        scoreboard.level_up()  
        scoreboard.update_score() 

screen.exitonclick()