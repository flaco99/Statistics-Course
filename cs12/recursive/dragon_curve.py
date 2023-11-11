import turtle

pen = turtle.Turtle()
pen.speed(0)

def dL(size, reverse):
    pen.forward(size)
    pen.right(90*reverse)
    pen.forward(size)

def dn(order, size, reverse):
    # base
    if order==0:
        dL(size, reverse)
        return
    else:
        dn(order-1, size, 1)
        pen.right(90*reverse)
        dn(order-1, size, -1)

dn(10, 10, 1)

turtle.done()