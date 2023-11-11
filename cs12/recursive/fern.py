import turtle

pen = turtle.Turtle()
pen.speed(0)
#pen.pensize(10)


def half_fern(size, branches, mirror):
    for i in range(branches):
        branch_size = size / ((i+1)*2)
        step_size = size / ((i+1)*2)
        pen.forward(step_size)
        pen.right(90*mirror)
        pen.forward(branch_size)
        pen.back(branch_size)
        pen.left(90*mirror)
        pen.forward(step_size)


def full_fern(size, branches):
    origin = pen.pos()
    half_fern(size, branches, 1)
    pen.goto(origin)

    origin = pen.pos()
    half_fern(size, branches, -1)
    pen.goto(origin)


def fern(size, branches, order):
    if order == 0:
        full_fern(size, branches)
        return
    else:
        for j in (1, -1):
            origin = pen.pos()
            for i in range(branches):
                branch_size = size / ((i + 1))
                step_size = size / (i + 1)
                pen.forward(step_size)
                pen.right(90*j)
                pen.forward(branch_size)
                pen.back(branch_size)

                fern(branch_size, branches, order-1)

                pen.left(90*j)
                pen.forward(step_size)
            pen.goto(origin)


fern(100, 3, 2)
turtle.done()