from turtle import Turtle

class Frog(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape('turtle')
    self.color('white')
    self.goto(0, -300)
    self.setheading(90)

  def go_forward(self): 
    self.setheading(90)
    self.move()
  
  def go_backward(self): 
    self.setheading(270)
    self.move()
  
  def go_right(self):
    self.setheading(0)
    self.move()
  
  def go_left(self):
    self.setheading(180)
    self.move()
  
  def move(self):
    self.forward(20)
  
  def restart(self):
    self.goto(0, -300)
    self.setheading(90)
