
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('white')
        self.goto(STARTING_POSITION)
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
        self.forward(MOVE_DISTANCE)
    
    def level_complete(self):
        self.goto(STARTING_POSITION)
