# Falling Sand Lab

import drawgrid2 as drawgrid
import random

EMPTY = "black"
METAL = "grey"
SAND = 'yellow'
WATER = 'blue'
PLANT = 'green'
WETSAND = 'orange'

STEPS_PER_FRAME = 3000

CANVAS_WIDTH = 60
CANVAS_HEIGHT = 60

canvas = []
row = [EMPTY]*CANVAS_WIDTH
for i in range(CANVAS_HEIGHT):
    canvas.append(row.copy())

brush = METAL


def paint(x, y):
    """Places the current brush material at location (x, y) on the canvas."""
    canvas[y][x] = brush


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

    if (y+1 < CANVAS_HEIGHT) and (pixel == SAND or pixel == WETSAND):
        if canvas[y+1][x] == EMPTY:
            canvas[y][x] = EMPTY
            canvas[y+1][x] = pixel
        elif canvas[y+1][x] == WATER:
            canvas[y][x] = WATER
            canvas[y+1][x] = pixel
        if count_touching(x, y, WATER) > 0:
            canvas[y][x] = WETSAND

    if pixel == WATER:
        new_loc = random.choice([(y, x-1), (y+1, x), (y+3, x), (y+4, x), (y+4, x), (y+3, x), (y+1, x), (y, x+1)])
        if (new_loc[0] < CANVAS_HEIGHT) and (new_loc[1] < CANVAS_WIDTH) and (new_loc[1] >= 0) and \
                (canvas[new_loc[0]][new_loc[1]] == EMPTY):
            canvas[y][x] = EMPTY
            canvas[new_loc[0]][new_loc[1]] = WATER
        elif (y+2 < CANVAS_HEIGHT) and (x+5 < CANVAS_WIDTH) and (x-5 >= 0) and (canvas[y+1][x] != EMPTY) \
                and (canvas[y+2][x] != EMPTY):
            randdirection = random.choice([1, -1])
            if randdirection == 1:
                if canvas[y][x+5] == EMPTY:
                    canvas[y][x] = EMPTY
                    canvas[y][x+5] = WATER
            else:
                if canvas[y][x-5] == EMPTY:
                    canvas[y][x] = EMPTY
                    canvas[y][x-5] = WATER

    if pixel == PLANT:
        if (y-1 > 0) and (count_touching(x, y, WATER) > 0):
            canvas[y - 1][x] = PLANT


def frame():
    """Calls the step function the number of times defined in the
       STEPS_PER_FRAME constant."""
    for j in range(STEPS_PER_FRAME):
        step()


def metal_brush():
    global brush
    brush = METAL


def sand_brush():
    global brush
    brush = SAND


def water_brush():
    global brush
    brush = WATER


def plant_brush():
    global brush
    brush = PLANT


def empty_brush():
    global brush
    brush = EMPTY


# Create the grid for drawing
drawing = drawgrid.Grid(canvas)

# Change the brush material when keys are pressed
drawing.onkey("m", metal_brush)
drawing.onkey("s", sand_brush)
drawing.onkey("w", water_brush)
drawing.onkey("p", plant_brush)
drawing.onkey("e", empty_brush)

# Finish setup and start the drawing
drawing.onclick(paint)
drawing.set_framerate(60)
drawing.set_update_while_draw(True)
drawing.start(frame)