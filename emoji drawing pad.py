import pygame
import pyperclip

pygame.init()

font = pygame.font.SysFont('comicsans', 20)
screen_width, screen_height = 250, 350
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
primary = '⬜'
secondary = '⬛'
rows = 7
cols = 5
def cleargrid(grid):
    grid.clear()
    for _ in range(rows):
        grid.append([secondary for _ in range(cols)])


def creategrid():
    grid = []
    # row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # don't ever try to make row by urself and then enter it 22 times
    for _ in range(rows):
        grid.append([secondary for _ in range(cols)])
    return grid

def grid_print(grid):
    string = ''
    for i in grid:
        for j in i:
            string += j
            print(j,end='')
        string += r'\n'
        print()
    pyperclip.copy(string)
grid = creategrid()
class box:  # 😂
    def __init__(self, emoji, width):
        self.x = None
        self.y = None
        self.index = []
        self.emoji = emoji
        self.secondary = secondary
        self.width = width
        self.color = (255, 255, 255)
        self.second_color = (255, 255, 100)
        self.border = 2
        self.clicked = False
    def draw(self, window, x, y, grid):
        self.x = x
        self.y = y
        pygame.draw.rect(window, self.color, (x, y, self.width, self.width))
        pygame.draw.rect(window, self.second_color, (x + (self.border * .5), y + (self.border * .5), self.width - self.border, self.width - self.border))

        if self.clicked:
            row, col = self.index
            grid[row][col] = self.emoji
            pygame.draw.rect(window, (255, 0, 0), (x + (7 * .5), y + (7 * .5), self.width - 5, self.width - 5))
            '''
            text = font.render('{}'.format(self.emoji), 1, (255, 0, 0))
            window.blit(text, (  (self.x + (self.width // 2)) - text.get_width() // 2,
                                 self.y + (self.width // 2) - text.get_height() // 2))
            '''
        else:
            try:
                row, col = self.index
                grid[row][col] = self.secondary
            except:
                pass
    def click(self, pos):
        mx, my = pos
        if self.x <= mx <= self.x + self.width:
            if self.y <= my <= self.y + self.width:
                self.clicked = True
    def unclick(self, pos):
        mx, my = pos
        if self.x <= mx <= self.x + self.width:
            if self.y <= my <= self.y + self.width:
                self.clicked = False
def drawAll(boxes, window, grid, columns):
    x = 0
    y = 0
    row = 0
    col = 0
    for i, bx in enumerate(boxes):
        bx.draw(window, x, y, grid)
        bx.index = [row, col]

        if (i + 1) % columns == 0 and i != 0:
            col = 0
            row += 1
            x = 0
            y += bx.width
        else:
            x += bx.width
            col += 1


def RedrawGameWindow(boxes):
    win.fill(0)
    drawAll(boxes, win, grid, 11)
    pygame.display.update()

def main():
    running = True
    boxes = [box(primary, 50) for _ in range(121)]
    printLoop = 0
    while running:
        clock.tick(30)
        RedrawGameWindow(boxes)
        if printLoop > 0:
            printLoop += 1
        if printLoop > 150:
            printLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                pos = pygame.mouse.get_pos()
                for bx in boxes:
                    bx.click(pos)
            elif mouse[2]:
                pos = pygame.mouse.get_pos()
                for bx in boxes:
                    bx.unclick(pos)
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE]:
            cleargrid(grid)
            for bx in boxes:
                bx.clicked = False
        elif key[pygame.K_RETURN] and printLoop == 0:
            grid_print(grid)
            print('\n\n')
            printLoop += 1


main()