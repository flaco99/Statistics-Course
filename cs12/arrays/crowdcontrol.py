import drawgrid2 as drawgrid
import random
# more readable

EMPTY = "black"
METAL = "grey"
HUMAN = 'yellow'
CRUSHED = 'red'
GOAL = 'green'

STEPS_PER_FRAME = 1000

CANVAS_WIDTH = 60
CANVAS_HEIGHT = 60

canvas = []
row = [EMPTY]*CANVAS_WIDTH
for i in range(CANVAS_HEIGHT):
    canvas.append(row.copy())

brush = GOAL


def paint(x, y):
    """Places the current brush material at location (x, y) on the canvas."""
    global goal_x
    global goal_y
    if (y < CANVAS_HEIGHT) and (x < CANVAS_WIDTH):
        canvas[y][x] = brush
    if brush == GOAL:
        goal_x = x
        goal_y = y


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


def step():
    """Chooses a random location on the canvas and updates it and any
       relevant surrounding pixels."""
    x = random.randint(0, CANVAS_WIDTH-1)
    y = random.randint(0, CANVAS_HEIGHT-1)
    pixel = canvas[y][x]
    if pixel == (HUMAN or CRUSHED):
        xdiff = goal_x - x
        ydiff = goal_y - y
        if abs(xdiff) > abs(ydiff):
            if abs(xdiff) > 1:
                xunitv = xdiff // abs(xdiff)
                if canvas[y][x+xunitv] == EMPTY:
                    move(x, y, x+xunitv, y)
                else:
                    pivot = random.choice([1])
                    if canvas[y+pivot][x] == EMPTY:
                        move(x, y, x, y+pivot)
        else:
            if abs(ydiff) > 1:
                yunitv = ydiff//abs(ydiff)
                if canvas[y+yunitv][x] == EMPTY:
                    move(x, y, x, y+yunitv)
                else:
                    pivot = random.choice([1])
                    if canvas[y][x+pivot] == EMPTY:
                        move(x, y, x+pivot, y)

        if count_touching(x, y, EMPTY) < 1:
            canvas[y][x] = CRUSHED


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

def goal_brush():
    global brush
    brush = GOAL

def empty_brush():
    global brush
    brush = EMPTY

# Create the grid for drawing
drawing = drawgrid.Grid(canvas)

# Change the brush material when keys are pressed
drawing.onkey("m", metal_brush)
drawing.onkey("h", human_brush)
drawing.onkey("g", goal_brush)
drawing.onkey("e", empty_brush)

# Finish setup and start the drawing
drawing.onclick(paint)
drawing.set_framerate(60)
drawing.set_update_while_draw(True)
drawing.start(frame)
