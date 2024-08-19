from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")





start_game=True
while start_game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    ##Detect collision with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.ball_bounce_y()
    ##Detect collison with paddle and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()

    if ball.xcor() > 380:
        ball.resetting()
        scoreboard.left_score()

    if ball.xcor() < -380:
        ball.resetting()
        scoreboard.ryt_score()





screen.exitonclick()

