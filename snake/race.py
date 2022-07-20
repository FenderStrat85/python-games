from turtle import Turtle, Screen
import random


screen = Screen()

# sets up size of screen
screen.setup(width=700, height=500)

is_race_on = False
colours =['red', 'orange', 'yellow', 'blue', 'purple', 'pink', 'green', 'black']
x_coord = -300
y_coord = 200
# text input 
user_bet = screen.textinput('Place your bets!', 'Which colour do you think will win? ')
all_turtle_list = []

for color in colours:
#  set turtle coordinate
  new_turtle = Turtle(shape='turtle')
  new_turtle.penup()
  new_turtle.color(color)
  new_turtle.goto(x_coord, y_coord)
  y_coord -= 50
  all_turtle_list.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtle_list:
    if turtle.xcor() > 300:
      is_race_on = False
      if(turtle.pencolor() == user_bet):
        print(f'You win a million pounds. The {turtle.pencolor()} turtle won')
      else:
        print(f'You lose all the money! The {turtle.pencolor()} turtle won')
    
    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)







screen.exitonclick()
