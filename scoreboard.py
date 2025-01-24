from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
    
    def update_score(self):
        self.clear()
        self.write(f"{self.score}", font=("Courier", 50, "normal"))

    def game_over(self, winner):    
        self.goto(0, 0)
        self.write("GAME OVER", font=("Courier", 50, "normal"), align="center")
        self.goto(0, -50)
        self.write(f"{winner} wins!", font=("Courier", 50, "normal"), align="center")

