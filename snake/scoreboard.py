from turtle import Turtle 

class Scoreboard(Turtle):
  def __init__(self):
      super().__init__()
      self.score = 0
      with open("high_score.txt") as file:
        self.high_score = int(file.read())
      self.penup()
      self.hideturtle()
      self.color('white')
      self.goto(0, 280)
  
  def increase_score(self):
    self.score += 10

  def update_scoreboard(self):
    self.clear()
    self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 15, 'normal'))

  def game_end(self):
    self.clear()
    self.write(f'Oh no! You died! Score: {self.score}', align='center', font=('Arial', 15, 'normal'))

  def game_reset(self):
    if self.score > self.high_score:
      with open("high_score.txt", mode="w") as file:
        file.write(str(self.score))
      with open("high_score.txt") as file:
        self.high_score = int(file.read())
    self.score = 0
    self.update_scoreboard() 