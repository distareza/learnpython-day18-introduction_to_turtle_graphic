"""
Challenge Draw Random Walk with random colour
https://en.wikipedia.org/wiki/Random_walk
https://docs.python.org/3/library/turtle.html#turtle.speed
https://docs.python.org/3/library/turtle.html#turtle.setheading
"""
import random
import turtle

thick = 8
distance = 50
step = 100

ink = turtle.Turtle()
ink.pensize(thick)
ink.speed(0.5)

direction = [0, 90, 180, 270]

def random_color():
    return random.random(), random.random(), random.random()

for _ in range(step):
    ink.pencolor(random_color())
    ink.setheading(random.choice(direction))
    ink.forward(distance)

print("done")
turtle.Screen().exitonclick()
