from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(0, -300)
        
    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        if self.ycor() > 350:
            self.goto(self.xcor(), 300)
            
    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
        if self.ycor() < -350:
            self.goto(self.xcor(), -300)
            
    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        if self.xcor() < -280:
            self.goto(-280, self.ycor())
            
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        if self.xcor() > 280:
            self.goto(280, self.ycor())
        
        