import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Turtle Race", prompt="Bet on the turtle that you think will win")
colors = ["red", "green", "orange", "blue", "purple", "yellow"]
all_turtle = []
j = -90
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-230, j)
    all_turtle.append(new_turtle)
    j += 30
if user_bet:
    is_race_on = True
while is_race_on:
    for _ in all_turtle:
        if _.xcor() >= 230:
            winning_color = _.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print("You've Won!!" + winning_color + "won")
            else:
                print("You've Lost!!" + winning_color + "won")
        rand_distance = random.randint(0, 10)
        _.forward(rand_distance)
screen.exitonclick()
