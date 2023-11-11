# use class


import drawgrid2 as drawgrid
import random

EMPTY = "black"
METAL = "grey"
HUMAN = 'yellow'

STEPS_PER_FRAME = 1000

CANVAS_WIDTH = 15
CANVAS_HEIGHT = 15

canvas = []
row = [EMPTY]*CANVAS_WIDTH
for i in range(CANVAS_HEIGHT):
    canvas.append(row.copy())


def paint(x, y):
    """Places the current brush material at location (x, y) on the canvas."""
    if (y < CANVAS_HEIGHT) and (x < CANVAS_WIDTH):
        canvas[y][x] = brush


def move(x1,y1,x2,y2):
    if (x2 < CANVAS_WIDTH) and (y2<CANVAS_HEIGHT):
        canvas[y1][x1] = EMPTY
        canvas[y2][x2] = HUMAN


def count_touching(x, y, substance):
    count = 0
    for (xp, yp) in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if 0 < xp < CANVAS_WIDTH and 0 < yp < CANVAS_HEIGHT:
            if canvas[yp][xp] == substance:
                count += 1
    return count


def setup():
    metal_brush()
    mid = CANVAS_WIDTH//2
    for x in [mid-3, mid-2, mid-1, mid+1, mid+2, mid+3]:
        for i in range(10):
            paint(x, i+3)
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(nums)


def spawn():
    mid = CANVAS_WIDTH // 2
    paint(mid, i+2)


def step():
    """Chooses a random location on the canvas and updates it and any
       relevant surrounding pixels."""
    x = random.randint(0, CANVAS_WIDTH-1)
    y = random.randint(0, CANVAS_HEIGHT-1)
    pixel = canvas[y][x]
    #if pixel == HUMAN:


def frame():
    """Calls the step function the number of times defined in the
       STEPS_PER_FRAME constant."""
    for j in range(STEPS_PER_FRAME):
        step()

def metal_brush():
    global brush
    brush = METAL

def human_brush():
    global brush
    brush = HUMAN

def empty_brush():
    global brush
    brush = EMPTY

# Create the grid for drawing
drawing = drawgrid.Grid(canvas)

# Change the brush material when keys are pressed
drawing.onkey("m", metal_brush)
drawing.onkey("e", empty_brush)

# Finish setup and start the drawing
setup()
drawing.onclick(paint)
drawing.set_framerate(60)
drawing.set_update_while_draw(True)
drawing.start(frame)
