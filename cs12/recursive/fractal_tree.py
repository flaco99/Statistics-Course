# Tree fractal drawing

import turtle

pen = turtle.Turtle()

def tree(order, branch_angle, size):
    """Draws a tree with segments of the given size"""
    if order == 0:
        # Base case: an order 0 tree is a straight line
        pen.forward(size)
        pen.back(size)
    else:
        # Recursive case:
        
        # draw a line forward
        pen.forward(size)

        # turn to the left, then draw a smaller tree
        pen.left(branch_angle)
        tree(order-1, branch_angle, size*0.7)

        # turn to the right, then draw a smaller tree
        pen.right(branch_angle*2)
        tree(order-1, branch_angle, size*0.7)

        # Turn back to face forward, then reverse to original position
        pen.left(branch_angle)
        pen.back(size)

tree(4, 90, 60)
