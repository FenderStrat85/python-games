from turtle import Turtle

class State_Writing(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.hideturtle()  
      
  def write_state(self, x, y, state_name):
      self.goto(x, y)
      self.write(state_name)

  def game_over(self):
    self.goto(0, 350)
    self.write('You got them all correct!')
