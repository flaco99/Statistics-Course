import random

EMPTY = ' '
MINE = '*'


def gen_board(width, height, mines):
    # create 2D array
    row = [EMPTY]*width
    board = []
    for i in range(height):
        board.append(row.copy())
    for j in range(mines):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        while board[y][x] != EMPTY:
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
        board[y][x] = MINE
    return board


def display_board(board, show_mines):
    width = len(board[0])
    line = '-'*(width+2)
    print(line)
    for row in board:
        row_str = '|'
        for item in row:
            if (not show_mines) and (item==MINE):
                row_str += EMPTY
            else:
                row_str += item
            #row_str += '|'
        print(row_str + '|')
    print(line)


def dig(board, x, y):
    cur_item = board[y][x]
    if cur_item==EMPTY:
        total_mines_around = 0
        for location in [(y, x+1), (y, x-1), (y+1, x), (y-1, x), (y+1, x+1), (y+1, x-1), (y-1, x+1), (y-1, x-1)]:
            if (location[0] < len(board)) and (location[1] < len(board[0])) and (board[location[0]][location[1]]==MINE):
                total_mines_around += 1
        board[y][x] = str(total_mines_around)
    elif cur_item==MINE:
        board[y][x] = 'X'