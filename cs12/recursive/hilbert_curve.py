import turtle

pen = turtle.Turtle()
pen.speed(0)

def h0(size, mirror):
    pen.forward(size)
    pen.left(90*mirror)
    pen.forward(size)
    pen.left(90*mirror)
    pen.forward(size)


def hn(order, size, mirror):
    # base
    if order == 0:
        h0(size, mirror)
        return

    is_odd = order % 2 == 1

    hn(order - 1, size, -mirror)
    if is_odd:
        pen.left(90*mirror)
    pen.forward(size)
    if not is_odd:
        pen.left(90*mirror)
    hn(order - 1, size, mirror)
    if is_odd:
        pen.right(90*mirror)
    pen.forward(size)
    if is_odd:
        pen.right(90*mirror)
    hn(order - 1, size, mirror)
    if not is_odd:
        pen.left(90*mirror)
    pen.forward(size)
    if is_odd:
        pen.left(90*mirror)
    hn(order - 1, size, -mirror)

def hilbert(order, size):
    return hn(order, size, 1)

hilbert(4, 5)
turtle.done()