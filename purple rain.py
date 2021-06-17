import pygame
from random import randint
# pybook
screenwidth = 500
screenheight = 500

pygame.init()
pygame.display.set_caption('Purple Rain')

clock = pygame.time.Clock()

win = pygame.display.set_mode((screenwidth,screenheight))

class drop:
    def __init__(self, x, y, len, width):
        self.x = x
        self.y = y
        self.len = len
        self.width = width
        self.vel = 0
        self.acc = ((self.width * self.len) * 0.02) * 0.15
    def draw(self, window):
        self.vel += self.acc
        self.y += self.vel
        if self.y > screenheight:
            self.y = randint(-90,-20)
            self.vel = 0
        pygame.draw.line(window, (138,43,226),(self.x, self.y), (self.x,self.y + self.len),self.width)
drops = []
for drp in range(301):
    drops.append(drop(randint(0,screenwidth),randint(-90,-20),randint(10,20),randint(4,8)))

dp = drop(20,20,20,7)
def RedrawGameWindow():
    win.fill((230,190,250))
    for drp in drops:
        drp.draw(win)
    dp.draw(win)
    pygame.display.update()
running = True
while running:
    clock.tick(60)
    RedrawGameWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False