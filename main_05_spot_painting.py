"""
Challenge spot color of a painting
    https://pypi.org/project/colorgram.py/
    1. extract a list of color (tuple) from an image
        utilize colorgram package

    2. start painting using turtle graphic
"""
import colorgram
import turtle

number_of_colors = 100

image_file = "image.jpg"


def extractColor():
    colors = colorgram.extract(image_file, number_of_colors)

    rgb_color = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_color += [(r, g, b)]

    return rgb_color


my_color = extractColor()

my_draw = turtle.Turtle()
turtle.colormode(255)
my_draw.speed(0)
my_draw.hideturtle()

step = 40
size = 20
step_width = 7

my_draw.penup()

counter = 0
my_draw.backward(step * step_width / 2)
while len(my_color) > 0:
    my_draw.pendown()
    my_draw.dot(size, my_color.pop())
    my_draw.penup()
    my_draw.forward(step)
    counter += 1
    if counter % step_width == 0:
        my_draw.backward(step * step_width)
        my_draw.setheading(90)
        my_draw.forward(step)
        my_draw.setheading(0)

print("done")
turtle.Screen().exitonclick()
