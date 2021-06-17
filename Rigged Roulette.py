import pygame
from math import sin, cos, pi, radians, degrees
pygame.init()
screen_width, screen_height = 600, 500
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
class roulette:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = screen_height // 2 - 100
        self.actualRadius = self.radius + 100
        self.color = (255, 0, 0)
        self.spin = 360
    def draw(self, window, time):
        self.drawLines(window, 6, ['win', 'lose', 'lose', 'lose', 'lose', 'lose'],time)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.actualRadius, 5)

    def drawLines(self, window, lines, titles, time):
        font = pygame.font.SysFont('comicsans', 200 // lines)
        change = 360 // lines
        start = -90 - (change // 2)
        for i in range(lines):
            # pygame.draw.line(window, self.color, (self.x, self.y), (self.x + self.radius * cos(radians(start - (360 // lines))), self.y + self.radius * sin(radians(start - (360 // lines)))))
            text_angle = radians(start + change // 2) + time
            text = font.render(str(titles[i]), True, (255, 255, 255))
            text = pygame.transform.rotate(text, -degrees(text_angle))
            win.blit(text, (self.x + self.radius * cos(text_angle) - text.get_width() // 2, self.y + self.radius * sin(text_angle) - text.get_height() // 2))
            pygame.draw.line(window, self.color, (self.x, self.y), (self.x + self.actualRadius * cos(radians(start) + time), self.y + self.actualRadius * sin(radians(start) + time)))
            start += change


def RedrawGameWindow(new_roulette, time):
    win.fill((0, 0, 0))
    new_roulette.draw(win, time)
    pygame.display.update()


def main():
    running = True
    new_roulette = roulette()
    time = 0
    speed = 5
    while running:
        if new_roulette.spin > 0:
            if new_roulette.spin <= 20:
                time += radians(speed // 5)
                new_roulette.spin -= speed // 5
            elif new_roulette.spin <= 40:
                time += radians(speed // 4)
                new_roulette.spin -= speed // 4
            elif new_roulette.spin <= 50:
                time += radians(speed // 3)
                new_roulette.spin -= speed // 3
            elif new_roulette.spin <= 100:
                time += radians(speed // 2)
                new_roulette.spin -= speed // 2
            else:
                time += radians(speed)
                new_roulette.spin -= speed
        RedrawGameWindow(new_roulette, time)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()