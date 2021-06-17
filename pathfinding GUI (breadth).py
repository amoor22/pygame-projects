import pygame
import queue
pygame.init()
# we can we will and we will conquer and we will reign supreme
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 'x', 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

path = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
clock = pygame.time.Clock()

screen_width, screen_height = 600, 600
win = pygame.display.set_mode((screen_width, screen_height))
class block:
    def __init__(self):
        self.x = None
        self.y = None
        self.index = []
        self.width = 40
        self.colors = [(0), (255, 0, 0), (0, 255, 0)]
        self.color = self.colors[0]
        self.clicked = False
        self.path = False
        self.edge = False
    def draw(self, window, x, y):
        self.x = x
        self.y = y
        self.color = self.colors[0]
        if self.edge:
            self.color = self.colors[1]
        else:
            try:
                row, col = self.index
                if path[row][col] == 1:
                    self.path = True
                else:
                    self.path = False
            except:
                pass
            if self.path:
                self.color = self.colors[2]
            elif self.clicked:
                row, col = self.index
                maze[row][col] = 0
                self.color = self.colors[1]
            else:
                try:
                    row, col = self.index
                    maze[row][col] = 1
                except:
                    pass
        pygame.draw.rect(window, self.color, (x, y, self.width, self.width))

    def click(self, pos):
        mx, my = pos
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.width:
                self.clicked = True
    def unclick(self, pos):
        mx, my = pos
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.width:
                self.clicked = False
def drawAll(blocks, window, n):
    row = 0
    col = 0
    x = 0
    y = 0
    for i, blck in enumerate(blocks):
        blck.draw(window, x, y)
        blck.index = [row, col]
        if (i + 1) > (n * n) - n:
            blck.edge = True
        if (i + 1) % n == 0 and i != 0:
            row += 1
            col = 0
            y += blck.width
            x = 0
            blck.edge = True
        else:
            col += 1
            x += blck.width
def RedrawGameWindow(blocks):
    win.fill(0)
    drawAll(blocks, win, 15)
    pygame.display.update()
def valid(maze, start, path):
    done = False
    possible = True
    row, col = start
    for j in path:
        if j == 'r':
            if maze[row][col + 1] == 'x':
                done = True
            if maze[row][col + 1] in [1, 'x'] and col < len(maze[0]) - 1:
                col += 1
            else:
                possible = False
        if j == 'l':
            if maze[row][col - 1] == 'x':
                done = True
            if maze[row][col - 1] in [1, 'x'] and col > 0:
                col -= 1
            else:
                possible = False
        if j == 'u':
            if maze[row - 1][col] == 'x':
                done = True
            if maze[row - 1][col] in [1, 'x'] and row > 0:
                row -= 1
            else:
                possible = False
        if j == 'd':
            if maze[row + 1][col] == 'x':
                done = True
            if maze[row + 1][col] in [1, 'x'] and row < len(maze) - 1:
                row += 1
            else:
                possible = False
    return possible, done, start
# print(valid(maze, [13, 0], 'rrrrrrrr'))
def solve(maze, start):
    done = False
    que = queue.Queue()
    que.put('')
    while not done:
        last = que.get()
        for i in ['r', 'l', 'u', 'd']:
            add = last + i
            validation = valid(maze, start, add)
            if validation[0]:
                que.put(add)
            if validation[1]:
                done = True
                print(add)
solve(maze, [11, 0])
def main():
    global maze, path
    running = True
    blocks = [block() for _ in range(225)]
    click_loop = 0
    while running:
        clock.tick(30)
        RedrawGameWindow(blocks)
        if click_loop > 0:
            click_loop += 1
        if click_loop > 10:
            click_loop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            m = pygame.mouse.get_pressed()
            if m[0]:
                m = pygame.mouse.get_pos()
                for blck in blocks:
                    blck.click(m)
            elif m[2]:
                m = pygame.mouse.get_pos()
                for blck in blocks:
                    blck.unclick(m)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN] and click_loop == 0:
            click_loop += 1
        elif key[pygame.K_BACKSPACE] and click_loop == 0:
            click_loop += 1
            maze = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            path = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]


# main()