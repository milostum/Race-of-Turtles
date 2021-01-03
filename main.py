#       []      {}
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x = - (screen.window_width() / 2) + 20
y = -100
turtles = []
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=x, y=y)
    y += 40

stop = False
while not stop:
    for turtle in turtles:
        speed = randint(0, 20)
        turtle.forward(speed)
        if turtle.xcor() >= (screen.window_width() / 2) - 25:
            stop = True
            if turtle.color()[0] == user_bet:
                print(f"You've won! The {turtle.color()[0]} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.color()[0]} turtle is the winner!")
            break

screen.exitonclick()
