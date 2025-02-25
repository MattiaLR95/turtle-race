from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
puntata = screen.textinput(title= "Bet", prompt= "Choose the turtle's color: ")


t = Turtle("turtle")
t.color("red")
t.penup()
t.goto(x = -240, y = 0)

screen.exitonclick()