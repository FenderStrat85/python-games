from turtle import Turtle


from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.current_level = 1
    
    def update_score(self):
        self.clear()
        self.write(f'Level: {self.current_level}', align='center', font=FONT)
    
    def level_up(self):
        self.current_level+=1

    def game_over(self):
        self.clear()
        # self.hideturtle()
        # self.penup()
        # self.goto(0, 0)
        self.write(f'Game over. You reached level {self.current_level}', align='center', font=FONT)

