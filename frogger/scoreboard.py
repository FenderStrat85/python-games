from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color('white')
    self.hideturtle()
    self.goto(0, 350)
    self.transport_score = 0
    self.frog_score = 0
  
  def update_score(self):
    self.clear()
    self.write(f'Transport {self.transport_score} : {self.frog_score} Frog', align='center', font=('Arial', 15, 'normal'))
  
  def frog_dies(self):
    self.transport_score +=1
  
  def frog_lives(self):
    self.frog_score +=1