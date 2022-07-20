from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake: 
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
  
  def create_snake(self):
    for position in STARTING_POSITIONS:
      new_piece = self.create_segment()
      new_piece.goto(position)
      self.segments.append(new_piece)
  
  def add_piece(self):
    tail = self.segments[(len(self.segments)-1)]
    new_x = tail.xcor()
    new_y = tail.ycor()
    new_piece = self.create_segment()
    new_piece.goto(new_x, new_y)
    self.segments.append(new_piece)

  def create_segment(self):
    new_piece = Turtle()
    new_piece.penup()
    new_piece.shape('square')
    new_piece.color('white')
    return new_piece
  

  def move(self):
    for seg_num in range (len(self.segments)-1,0,-1):
      new_x = self.segments[seg_num-1].xcor()
      new_y = self.segments[seg_num-1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
  
  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90)

  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)
  
  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0)
  
  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180)

  def reset(self):
    for seg in self.segments:
      seg.goto(1000, 1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]
 