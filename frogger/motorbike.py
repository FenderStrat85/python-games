from turtle import Turtle

class Motorbike(Turtle):
  def __init__(self, starting_position):
    super().__init__()
    self.color('black')
    self.shape('square')
    self.penup()
    self.shapesize(stretch_wid=0.5, stretch_len=2)
    self.goto(starting_position)

  def move_forward(self):
    self.forward(20)