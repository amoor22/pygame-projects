import pygame
import random
import math
pygame.init()
# never ever use photoshop's rectangle it doesn't work with masks

screen_width, screen_height = 500, 500

win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

dart_num = 20000
font = pygame.font.SysFont('comicsans', 30)

class dart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.hypot(self.x - (screen_width // 2), self.y - (screen_height // 2))
    def draw(self, window):
        window.fill((255, 0, 0), ((self.x, self.y), (1, 1)))
def RedrawGameWindow(PI):
    text = font.render(f'{round(PI, 5)}', 1, (255, 255, 255))
    padding_rect = 5
    pygame.draw.rect(win, (0, 0, 0), ((screen_width // 2 - text.get_width() // 2) - padding_rect, (screen_width // 2 - text.get_height() // 2) - padding_rect, text.get_width() + padding_rect * 2, text.get_height() + padding_rect * 2))
    win.blit(text, (screen_width // 2 - text.get_width() // 2, screen_width // 2 - text.get_height() // 2))
    print(PI)
    pygame.display.update()


def main():
    running = True
    # darts = [dart(random.randint(0, screen_width), random.randint(0, screen_width)) for x in range(2000)]
    darts = 0
    inside = 0
    all_b = 0
    PI = 0
    while running:
        # clock.tick(600)
        RedrawGameWindow(PI)
        pygame.draw.circle(win, (255, 255, 255), (screen_width // 2, screen_height // 2), screen_width // 2, 1)
        if darts < dart_num:
            d = dart(random.randint(0, screen_width), random.randint(0, screen_width))
            d.draw(win)
            if d.distance < screen_width // 2:
                inside += 1
            all_b += 1
            PI = (inside / all_b) * 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
