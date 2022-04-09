"""
Introduction to Turtle Graphic
https://docs.python.org/3/library/turtle.html

"""
from turtle import Turtle, Screen

turtle = Turtle()

turtle.shape("turtle")
turtle.color("green")

# Draw Square
for _ in range(4) :
    turtle.forward(100)
    turtle.left(90)


Screen().exitonclick()
