from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.speed(0)
        self.penup()



    def up(self):
        if self.ycor() >= 335:
            self.setposition(self.xcor(),self.ycor())
        else:
            new_y = self.ycor()+30
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() <= -330:
            self.setposition(self.xcor(),self.ycor())
        else:
            new_y = self.ycor()-30
            self.goto(self.xcor(), new_y)
