import pygame
import random
from math import hypot
screen_width = 400
screen_height = 400

green = (0, 255, 0)
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


def drawDots(n):
    dots = []
    for i in range(n):
        dot = pygame.draw.circle(win, green, (random.randint(1, screen_width), random.randint(1, screen_height)), 3)
        dots.append(dot)
    return dots
def noise(dots):
    for i in range(screen_width):
        for j in range(screen_height):
            distances = []
            for dot in dots:
                distance = hypot(i - dot.x, j - dot.y)
                distances.append(distance)
            distances.sort()
            color = int(distances[0])
            if color > 255:
                color = 255
            win.fill((color, color, color), ((i, j), (1, 1)))
noise(drawDots(9))


def RedrawGameWindow():
    # win.fill(256)
    pygame.display.update()


def main():
    running = True
    while running:
        clock.tick(60)
        RedrawGameWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()