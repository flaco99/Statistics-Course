# Koch fractal drawing

import turtle

pen = turtle.Turtle()
pen.speed(10)

def koch(order, size):
    """
    Make turtle tortoise draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    if order == 0: # The base case is just a straight line
        pen.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(order - 1, size / 3)
            pen.left(angle)

koch(3, 200)
