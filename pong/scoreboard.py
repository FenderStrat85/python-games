from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color('white')
    self.hideturtle()
    self.goto(0, 350)
    self.right_score = 0
    self.left_score = 0
  
  def update_score(self):
    self.clear()
    self.write(f'{self.left_score} : {self.right_score}', align='center', font=('Arial', 15, 'normal'))
  
  def right_scores(self):
    self.right_score += 1
  
  def left_scores(self):
    self.left_score += 1