import pygame
from random import randint
from queue import Queue
pygame.init()

screen_width, screen_height = 500, 500
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
row_col = 9
font = pygame.font.SysFont('comicsans', row_col * 3)
board = [[0 for i in range(row_col)] for _ in range(row_col)]
class block:
    def __init__(self):
        self.x = None
        self.y = None
        self.index = None
        self.width = 40
        self.margin = int(self.width * 0.1)
        self.small_width = self.width - (self.margin * 2)
        self.small_x = None
        self.small_y = None
        self.clicked = False
        self.color = (255, 255, 255)
        self.neighbours = 0
        self.other_color = (0, 255, 255)
        self.mine = False

    def draw(self, window, x, y):
        self.x = x
        self.y = y
        self.small_x = self.x + self.margin
        self.small_y = self.y + self.margin
        row, col = self.index
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.width, self.width))
        if not self.clicked:
            pygame.draw.rect(window, self.color, (self.small_x, self.small_y, self.small_width, self.small_width))
        else:
            if board[row][col] == 1:
                pygame.draw.rect(window, (255, 0, 255), (self.small_x, self.small_y, self.small_width, self.small_width))
            else:
                if self.neighbours > 0:
                    text = font.render(f'{self.neighbours}', True, (255, 0, 0))
                    win.blit(text, (self.small_x + (self.small_width // 2) - text.get_width() // 2, self.small_y + (self.small_width // 2) - text.get_height() // 2))

    def click(self, pos, blocks):
        mx, my = pos
        if self.small_x < mx < self.small_x + self.small_width:
            if self.small_y < my < self.y + self.small_width:
                self.clicked = True
                self.neighbours = neighbour(board, self.index)
                if self.neighbours == 0 and not self.mine:
                    breadth(self.index, blocks)
                    for i in empty:
                        for b in blocks:
                            if b.index == i and b.neighbours == 0:
                                b.clicked = True
                    for j in edges:
                        for b in blocks:
                            if b.index == j:
                                b.clicked = True

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
def grid_draw(blocks, rowcol):
    x = (screen_width - (blocks[0].width * rowcol)) // 2
    xC = x
    y = (screen_width - (blocks[0].width * rowcol)) // 2
    row = 0
    col = 0
    for i, b in enumerate(blocks):
        b.index = [row, col]
        b.draw(win, x, y)
        b.neighbours = neighbour(board, b.index)
        if board[row] [col] == 1:
            b.mine = True
        if (i + 1) % rowcol == 0:
            y += b.width
            x = xC
            row += 1
            col = 0
        else:
            col += 1
            x += b.width
def RedrawGameWindow(blocks):
    win.fill((255, 255, 0))
    grid_draw(blocks, row_col)
    pygame.display.update()
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
edges = []
def valid(board, start, path, blocks):
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
        for b in blocks:
            if b.neighbours > 0 and b.index in current_empty:
                edges.append(b.index)
                current_empty.remove(b.index)
    if len(current_empty) == 0:
        return False
    else:
        empty.extend(current_empty)
        return True
def breadth(start, blocks):
    que = Queue()
    que.put('')
    while True:
        current = que.get()
        for i in ['r', 'd', 'u', 'l' ]:
            #, 'q', 'e', 'z', 'x'
            if valid(board, start, current + i, blocks):
                que.put(current + i)
        if que.qsize() == 0:
            break

put_mines2(board, 2)
board_print(board)
def main():
    running = True
    blocks = [block() for _ in range(81)]
    loop = 0
    while running:
        RedrawGameWindow(blocks)
        clock.tick(60)
        if loop > 0:
            loop += 1
        if loop > 15:
            loop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        m = pygame.mouse.get_pressed()
        if m[0] and loop == 0:
            loop += 1
            pos = pygame.mouse.get_pos()
            for b in blocks:
                b.click(pos, blocks)

main()