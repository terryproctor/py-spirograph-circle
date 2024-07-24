from turtle import Turtle, Screen
import random

screen = Screen()
# screen.colormode(255)

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()

def make_circle():
    timmy.circle(100)
    
def change_tilt():
    timmy.left(5)

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    timmy.color(R, G, B)

def circle_spiro():
    for _ in range(72):
        change_color()
        make_circle()
        change_tilt()
    screen.exitonclick()
    

circle_spiro()
