from turtle import Turtle

class Car(Turtle):
  def __init__(self, starting_position):
    super().__init__()
    self.color('blue')
    self.shape('square')
    self.penup()
    self.shapesize(stretch_wid=1, stretch_len=3)
    self.goto(starting_position)
  
  def move_backward(self):
    self.backward(30)