import turtle

pen = turtle.Turtle()
pen.speed(5)

def ct(order, size):
    """
    Make turtle draw a Cesaro torn line fractal of 'order' and 'size'.
    """
    if order == 0: # The base case is just a straight line
        pen.forward(size)
    else:
        for angle in [-85, 170, -85, 0]:
            ct(order - 1, size / 3)
            pen.left(angle)

ct(3, 200)