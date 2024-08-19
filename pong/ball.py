from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.inc_x=10
        self.inc_y=10
        self.ball_speed=0.1


    def move(self):
        new_x=self.xcor()+self.inc_x
        new_y=self.ycor()+self.inc_y
        self.goto(new_x,new_y)

    def ball_bounce_y(self):
        self.inc_y*=-1

    def ball_bounce_x(self):
        self.inc_x*=-1
        self.ball_speed *= 0.9


    def resetting(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.ball_bounce_x()

