from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(10)

def move_backward():
  tim.backward(10)

def turn_clockwise():
  tim.right(10)

def turn_anticlockwise():
  tim.left(10)

def clear_screen():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_clockwise, 'd')
screen.onkey(turn_anticlockwise, 'a')
screen.onkey(clear_screen, 'c')
screen.exitonclick()