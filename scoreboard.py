from turtle import Turtle

with open("high_score.txt") as high_score_file:
    high_score = int(high_score_file.read())


highscoredoc = open("high_score.txt")
highscore = int(highscoredoc.read())
highscoredoc.close()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = highscore
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_scoreboard()
        with open("high_score.txt", mode="w") as high_score_file:
            high_score_file.write(f"{self.high_score}")
