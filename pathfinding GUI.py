import pygame
pygame.init()
# we can we will and we will conquer and we will reign supreme
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
def find_path(path, maze, row, col, endpoint):
    if [row, col] == endpoint:
        path[row][col] = 1
        return True
    if maze[row][col] == 1:
        path[row][col] = 1
        if find_path(path, maze, row, col + 1, endpoint):
            return True
        if find_path(path, maze, row + 1, col, endpoint):
            return True
        path[row][col] = 0
    return False


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
            find_path(path, maze, 0, 0, [13, 13])
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


main()