# Zhyldyz Torogulova
# 11/5/2025
# Problem 5: Use the following chunk of code as a base to produce the image shown below

import turtle


def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


wm = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
for size in [20, 40, 60, 80, 100]:
    drawSquare(alex, size)
    alex.penup()
    alex.goto(-size / 2, -size / 2)  # Move to top-left corner of the square
    alex.pendown()

wm.exitonclick()
