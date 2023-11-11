import drawgrid1 as drawgrid
import copy

DEAD = 'black'
ALIVE = 'white'

width = 100
height = 100

board = []
row = [DEAD]*width
for i in range(height):
    board.append(row.copy())


def count_neighbours(grid, x, y):
    count = 0
    for location in [(y, x+1), (y, x-1), (y+1, x), (y-1, x), (y+1, x+1), (y+1, x-1), (y-1, x+1), (y-1, x-1)]:
        if (location[0] < len(board)) and (location[1] < len(board[0])) and (
                board[location[0]][location[1]] == ALIVE):
            count += 1
    return count


def step():
    previous_grid = copy.deepcopy(board)
    for x in range(width):
        for y in range(height):
            neighbours = count_neighbours(previous_grid, x, y)
            if (board[y][x] == ALIVE) and (neighbours not in [2, 3]):
                board[y][x] = DEAD
            elif (board[y][x] == DEAD) and (neighbours == 3):
                board[y][x] = ALIVE


def set_alive(x, y):
    board[y][x] = ALIVE


drawing = drawgrid.Grid(board)
drawing.onclick(set_alive)
drawing.set_framerate(5)
drawing.start(step)