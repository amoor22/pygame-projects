import pygame
from random import randint
from math import hypot
pygame.init()

screen_width, screen_height = 500, 500
clock = pygame.time.Clock()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Classera 404')
min_radius, max_radius = 5, 15
min_vel, max_vel = 0.3, 2
max_line = 150
# velocity depends on radius
# color transparency depends on radius


def map_val(val, a, b, c, d):
    val2 = (val - a) / (b - a) * (d - c) + c
    return val2
class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = randint(min_radius, max_radius)
        self.velocity = map_val(self.radius, min_radius, max_radius, min_vel, max_vel)
        self.color = (255, 255, 255)
        self.lines_with = []

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        self.move()

    def move(self):
        if self.y + self.radius < 0:
            self.radius = randint(min_radius, max_radius)
            self.velocity = map_val(self.radius, min_radius, max_radius, min_vel, max_vel)
            self.y = screen_height + self.radius + randint(1, 15)
        self.y -= self.velocity
def get_distance(ball1, ball2):
    return hypot(ball1.x - ball2.x, ball1.y - ball2.y)
def draw_lines(window, balls):
    # for bll in balls:
    #     closest = None
    #     distance = screen_height * 30
    #     for bll2 in balls:
    #         if get_distance(bll, bll2) < distance:
    #             closest = bll2
    max_distance = max_line
    for bll in balls:
        for bll2 in balls:
            if get_distance(bll, bll2) <= max_distance:
                pygame.draw.line(window, (255, 255, 255), (bll.x, bll.y), (bll2.x, bll2.y))
def RedrawGameWindow(balls):
    win.fill(0)
    for bll in balls:
        bll.draw(win)
    draw_lines(win, balls)
    pygame.display.update()

def main():
    running = True
    balls = [ball(randint(-min_radius, screen_width + min_radius), randint(screen_height, screen_height + max_vel)) for i in range(30)]
    while running:
        clock.tick(60)
        RedrawGameWindow(balls)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
main()