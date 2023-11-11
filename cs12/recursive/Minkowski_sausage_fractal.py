import turtle

pen = turtle.Turtle()
pen.speed(5)

def mink(order, size):
    """
    Make turtle draw a Minkowski Sausage fractal of 'order' and 'size'.
    """
    if order == 0: # The base case is just a straight line
        pen.forward(size)
    else:
        for angle in [90, -90, -90, 0, 90, 90, -90, 0]:
            mink(order - 1, size / 3)
            pen.left(angle)

mink(2, 150)