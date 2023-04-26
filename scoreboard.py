from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0,300)
        self.score_player1 = 0
        self.score_player2 = 0
        self.write(f"{self.score_player1}     {self.score_player2}", align="center", font=("Courier", 100))




    def update_scoreboard(self,player1,player2):
        self.score_player1 = player1
        self.score_player2 = player2

        self.clear()
        self.write(f"{self.score_player1}     {self.score_player2}", align="center", font=("Courier", 100))


    def game_over(self,pl):
        self.setposition(0,0)

        self.write(f"Game Over Player{pl} win !!!", align="center", font=("Courier", 40))


