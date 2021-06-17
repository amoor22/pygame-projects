from random import randint
from queue import Queue
row_col = 9
board = [[0 for i in range(row_col)] for _ in range(row_col)]
def put_mines(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            rand = randint(0, 3)
            if rand == 1:
                board[row][col] = 1
def put_mines2(board, mines):
    mined = []
    for i in range(mines):
        while True:
            # randint is inclusive of both start and end numbers
            row, col = randint(0, len(board) - 1), randint(0, len(board[0]) - 1)
            if (row, col) not in mined:
                board[row][col] = 1
                mined.append((row, col))
                break
def board_print(board):
    for j in board:
        print(*j)
def expand_from(board, pos):
    row, col = pos
    empty = []
    for rw in range(row + 1, len(board)):
        if board[rw][col] == 0:
            empty.append([rw, col])
        else:
            break
    for rw in range(row):
        if board[rw][col] == 0:
            empty.append([rw, col])
        else:
            break
    for cl in range(col):
        if board[row][cl] == 0:
            empty.append([row, cl])
        else:
            break
    for cl in range(col + 1, len(board[0])):
        if board[row][cl] == 0:
            empty.append([row, cl])
        else:
            break
    return empty
def neighbour(board, pos):
    row, col = pos
    mines = 0
    if col < len(board[0]) - 1:
        if row > 0:
            if board[row - 1][col + 1] == 1:
                mines += 1
        if row < len(board) - 1:
            if board[row + 1][col + 1] == 1:
                mines += 1
        if board[row][col + 1] == 1:
            mines += 1
    if col > 0:
        if row > 0:
            if board[row - 1][col - 1] == 1:
                mines += 1
        if row < len(board) - 1:
            if board[row + 1][col - 1] == 1:
                mines += 1
        if board[row][col - 1] == 1:
            mines += 1
    if row < len(board) - 1:
        if board[row + 1][col] == 1:
            mines += 1
    if row > 0:
        if board[row - 1][col] == 1:
            mines += 1
    return mines
empty = []
def expand_recursion(board, pos):
    row, col = pos
    current_empty = []
    if col < len(board[0]) - 1:
        if board[row][col + 1] == 0:
            # print(row, col + 1)
            print(row, col + 1)
            current_empty.append([row, col + 1])
            expand_recursion(board, [row, col + 1])
    # if col > 0:
    #     if board[row][col - 1] == 0:
    #         current_empty.append([row, col - 1])
    #         expand_recursion(board, [row, col - 1])
    # if row < len(board) - 1:
    #     if board[row + 1][col] == 0:
    #         current_empty.append([row + 1, col])
    #         expand_recursion(board, [row + 1, col])
    # if row > 0:
    #     if board[row - 1][col] == 0:
    #         current_empty.append([row - 1, col])
    #         expand_recursion(board, [row - 1, col])
    return empty
    # if len(current_empty) > 0:
    #     expand_recursion(board)
def valid(board, start, path):
    row, col = start
    current_empty = []
    for i in path:
        if i == 'r':
            if col < len(board[0]) - 1:
                col += 1
        elif i == 'l':
            if col > 0:
                col -= 1
        elif i == 'u':
            if row > 0:
                row -= 1
        elif i == 'd':
            if row < len(board) - 1:
                row += 1
        elif i == 'q':
            if row > 0 and col > 0:
                row -= 1
                col -= 1
        elif i == 'e':
            if row > 0 and col < len(board[0]) - 1:
                row -= 1
                col += 1
        elif i == 'z':
            if row < len(board) - 1 and col > 0:
                row += 1
                col -= 1
        elif i == 'x':
            if row < len(board) - 1 and col < len(board[0]) - 1:
                row += 1
                col += 1
        if board[row][col] == 0:
            if [row, col] not in empty:
                current_empty.append([row, col])
    if len(current_empty) == 0:
        return False
    else:
        empty.extend(current_empty)
        return True
def breadth(start):
    que = Queue()
    que.put('')
    while True:
        current = que.get()
        valids = []
        for i in ['r', 'd', 'u', 'l', 'q', 'e', 'z', 'x']:
            if valid(board, start, current + i):
                que.put(current + i)
                valids.append(i)
        if que.qsize() == 0:
            break
        valids.clear()
put_mines2(board, 15)
breadth([0, 0])
print(empty)
def ass():
    for i in empty:
        row, col = i
        board[row][col] = 'x'

board_print(board)
ass()
print()
board_print(board)
