from turtle import Turtle

class Lorry(Turtle):
  def __init__(self, starting_position):
    super().__init__()
    self.color('orange')
    self.shape('square')
    self.penup()
    self.shapesize(stretch_wid=2, stretch_len=4)
    self.goto(starting_position)
  
  def move_forward(self):
    self.forward(20)
    # self.forward(20)
    # self.setheading(90)
    # self.forward(20)
    # self.setheading(0)
    # self.forward(20)
    # self.setheading(270)
    # self.forward(40)
    # self.setheading(0)
    # self.forward(20)
    # self.setheading(90)
    # self.forward(20)
    # self.setheading(0)

