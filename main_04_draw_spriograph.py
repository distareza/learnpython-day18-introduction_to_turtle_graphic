"""
Challenge to draw a Spirograph

"""

import random
import turtle
from turtle import Turtle, Screen

thick = 2
distance = 50
step = 100
loop = 100

loop_step = 360 / loop


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


ink = Turtle()
turtle.colormode(255)
ink.pensize(thick)
ink.speed(0)

position = 0
for _ in range(loop):
    ink.setheading(position)
    ink.pencolor(random_color())
    ink.circle(120)
    position += loop_step

print("done")
Screen().exitonclick()
