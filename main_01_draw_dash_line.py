"""
Challenge No. 1 Draw a Dash Line
hint :
        https://docs.python.org/3/library/turtle.html#turtle.forward
        https://docs.python.org/3/library/turtle.html#turtle.pen
        https://docs.python.org/3/library/turtle.html#turtle.pendown
        https://docs.python.org/3/library/turtle.html#turtle.penup
"""
import turtle as t

ink = t.Turtle()

for _ in range(15):
    ink.forward(10)
    ink.penup()
    ink.forward(10)
    ink.pendown()





t.Screen().exitonclick()