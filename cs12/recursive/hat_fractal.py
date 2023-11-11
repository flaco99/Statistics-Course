import turtle

pen = turtle.Turtle()
pen.speed(5)

def hat(order, size):
    """
    Make turtle draw a Hat fractal of 'order' and 'size'.
    """
    if order == 0: # The base case is just a straight line
        pen.forward(size)
    else:
        for angle in [90, -90, -90, 90, 0]:
            hat(order - 1, size / 3)
            pen.left(angle)

hat(3, 100)