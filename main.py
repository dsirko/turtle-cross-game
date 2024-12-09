from turtle import Turtle, Screen
from player import Player
import random

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("white")
screen.title("Turtle cross")
# screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")



screen.mainloop()