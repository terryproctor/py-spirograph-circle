from turtle import Turtle, Screen
import random, math as Math

screen = Screen()
# screen.colormode(255)

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()

def make_circle(width):
    timmy.circle(width)
    
def change_tilt(tilt):
    timmy.left(tilt)

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    timmy.color(R, G, B)

def circle_spiro(width, tilt):
    for _ in range(Math.ceil(360/tilt)):
        change_color()
        make_circle(width)
        change_tilt(tilt)
    screen.exitonclick()
    

circle_spiro(150, 0.5)
