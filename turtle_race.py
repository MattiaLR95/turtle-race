from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
puntata = screen.textinput(title= "Bet", prompt= "Choose the turtle's color: ")
colori = ["red", "green", "purple", "yellow", "blue", "magenta"]
pos_y = [0, -25, -50, 25, 50, 75]

turtles = []
for num in range(6):
    t = Turtle(shape= "turtle")
    t.color(colori[num])
    t.penup()
    t.goto(x = -240, y = pos_y[num])
    turtles.append(t)

start = True
while start:
    for turtle in turtles:
        if turtle.xcor() > 230:
            start= False
            if puntata == turtle.pencolor():
                print("You Win!!")
            else:
                print("You Lost")
        turtle.forward(randint(0,10))

screen.exitonclick()