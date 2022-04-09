"""
Challenge Draw Triangle, Square, Pentagon, Hexagon, heptagon, octagon, nanogon and decagon
and each of shape colour with random
hint : https://docs.python.org/3/library/turtle.html#turtle.right
"""
import turtle as t
import random

color = ["dark red", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "brown"]
pen = t.Turtle()
size = 100

for sides in range(3, 11):
    angle = 360 / sides
    pen.color(random.choice(color))
    for _ in range(sides):
        pen.forward(size)
        pen.right(angle)

t.Screen().exitonclick()