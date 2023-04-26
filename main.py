from turtle import Turtle, Screen
from padlle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("🔥 Pong game 🏓")
screen.tracer(0)

# Scoreboard
scoreboard = Scoreboard()


# middle line

middle_line = Turtle()
middle_line.goto(0, -400)
middle_line.speed(0)
middle_line.shape("square")
middle_line.color("white")
middle_line.shapesize(0.25, 1)
middle_line.penup()
middle_line.left(90)

for i in range(21):
    middle_line.forward(20)
    middle_line.stamp()
    middle_line.forward(20)

# Players
player1 = Paddle()
player1.goto(-550, 0)

player2 = Paddle()
player2.goto(550, 0)
# Ball
ball = Ball()

# Game setup
screen.listen()
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")



def start_game():
    game_on = True
    score_p1 = 0
    score_p2 = 0
    while game_on == True:

        ball.move()
        screen.update()
        time.sleep(0.05)
        # detetct collision with  wall
        if ball.ycor() >= 400 or ball.ycor() <= -400:
            ball.bounce_y()
        if ball.distance(player1) < 50 and ball.xcor() > -560 or ball.distance(player2) < 50 and ball.xcor() < 560:
            ball.bounce_x()
        if ball.xcor() == 600:
            score_p1 += 1
            scoreboard.update_scoreboard(score_p1,score_p2)
            player1.goto(-550, 0)
            player2.goto(550, 0)
            ball.reset_position()

        if ball.xcor() == -600:
            score_p2 += 1
            scoreboard.update_scoreboard(score_p1,score_p2)
            player1.goto(-550, 0)
            player2.goto(550, 0)
            ball.reset_position()
        if score_p1 == 5:
            middle_line.clear()
            scoreboard.game_over(1)
            game_on = False
        if score_p2 == 5:
            middle_line.clear()
            scoreboard.game_over(2)
            game_on = False










start_game()

screen.exitonclick()
