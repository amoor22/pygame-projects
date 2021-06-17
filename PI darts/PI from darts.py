import pygame
import random
from time import sleep
from math import sqrt
pygame.init()
# never ever use photoshop's rectangle it doesn't work with masks

screen_width, screen_height = 500, 500

win = pygame.display.set_mode((screen_width, screen_height))

dart_image = pygame.image.load('circ_0000_Ellipse-1.png')
circle_image = pygame.image.load('circle.png')

clock = pygame.time.Clock()

dart_num = 20000
font = pygame.font.SysFont('comicsans', 30)

class shape:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = screen_width
        self.radius = int(self.width / 2)
        self.color = (255, 255, 255)
        self.circle = circle_image
        self.mask = pygame.mask.from_surface(self.circle)
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width), 1)
        window.blit(self.circle, (0, 0))

    def hit(self, darts):
        inside = 0
        outside = 0
        for drt in darts:
            offset = (self.x - drt.x, self.y - drt.y)
            # result = sqrt((drt.x ** 2) + (drt.y ** 2)) < 500 # this works 2 although I don't know why
            # since the radius is 250 not 500
            result = drt.mask.overlap(self.mask, offset)
            if result:
                inside += 1
            outside += 1
        try:
            return round((inside / outside) * 4, 3)
        except:
            pass

class dart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = dart_image
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # def mask(self):
    #     return pygame.mask.from_surface(self.img)

def RedrawGameWindow(shape, darts):
    win.fill(0)
    shape.draw(win)
    for drt in darts:
        drt.draw(win)
    PI = font.render('PI? {}'.format(shape.hit(darts)), 1, (255,255,255))
    win.blit(PI, (screen_width//2 - PI.get_width()//2, 20))
    pygame.display.update()


def main():
    running = True
    shp = shape()
    # darts = [dart(random.randint(0, screen_width), random.randint(0, screen_width)) for x in range(2000)]
    darts = []
    while running:
        clock.tick(60)
        RedrawGameWindow(shp, darts)
        if len(darts) < dart_num:
            darts.append(dart(random.randint(0, screen_width), random.randint(0, screen_width)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
