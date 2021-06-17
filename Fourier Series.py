import pygame
import math
pygame.init()

clock = pygame.time.Clock()
screen_width, screen_height = 700, 500
win = pygame.display.set_mode((screen_width, screen_height))
class circle:
    def __init__(self, radius, color, filled):
        self.x = 0
        self.y = 0
        self.radius = radius
        self.filled = filled
        self.color = color
    def draw(self, window, x, y):
        self.x = x
        self.y = y
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius, self.filled)
xs = screen_width - 200
dots = []
time, time2 = 0, 0
num = 5
def RedrawGameWindow(circles):
    global time, time2
    win.fill(0)
    x1, y1 = 200, 200
    for i in range(num):
        n = i * 2 + 1
        prevx = x1
        prevy = y1
        radius = 50 * (4 / (n * math.pi))
        x1 += radius * math.cos(n * time)
        y1 += radius * math.sin(n * time)
        pygame.draw.circle(win, (255, 100, 0), (prevx, prevy), radius, 1)
        pygame.draw.line(win, (255, 255, 255), (prevx, prevy), (x1, y1))
        # prevx = x1
        # prevy = y1
    dots.append([xs, y1])
    pygame.draw.line(win, (255, 255, 255), (x1, y1), (xs, y1))
    # r1, r2, r3 = 50, 15, 5
    # x1, y1 = 200, 200
    # x2, y2 = x1 + (r1 * math.cos(time)), y1 + (r1 * math.sin(time))
    # x3, y3 = x2 + (r2 * math.cos(time2)), y2 + (r2 * math.sin(time2))
    for dot in range(len(dots) - 1):
        X, Y = dots[dot]
        X2, Y2 = dots[dot + 1]
        pygame.draw.line(win, (255, 255, 255), (X, Y), (X2, Y2))
        win.fill((255, 255, 255), ((X, Y), (1, 1)))
        dots[dot][0] += 0.2
    # pygame.draw.circle(win, (255, 0, 100), (x1, y1), r1, 1)
    # pygame.draw.circle(win, (255, 100, 0), (x2, y2), r2, 1)
    # # pygame.draw.circle(win, (0, 100, 255), (x3, y3), r3, 1)
    # pygame.draw.line(win, (255, 0, 0), (x2, y2), (x, y2))
    # dots.append([xs, y2])
    if len(dots) > 1000:
        dots.pop(0)
    time += 0.02
    time2 += 0.05
    pygame.display.update()


def main():
    running = True
    circles = [circle(50, (200, 0, 200), 1), circle(10, (200, 0, 200), 0)]
    while running:
        RedrawGameWindow(circles)
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()