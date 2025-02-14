from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.speed("fastest")
        self.paddle.shape("square")
        self.paddle.color("white")  
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto((position))

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)
    
    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
    