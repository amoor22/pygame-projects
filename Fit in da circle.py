import pygame
from random import randint
pygame.init()
font = pygame.font.SysFont('comicsans', 30)
screen_width = 500
screen_height = 500

red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

marginError = 20


class border:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.minRadius = 20
        self.maxRadius = 150
        self.radius = randint(self.minRadius, self.maxRadius)
        self.color = red

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius, 1)


class circle:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 1
        self.color = red
        self.score = 0
    def draw(self, window):
        self.move()
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.radius += 1

    def pop(self, bord):
        if bord.radius - self.radius <= marginError:
            self.score += 5
        else:
            self.die(bord)
        self.radius = 1
        bord.radius = randint(bord.minRadius, bord.maxRadius)

    def check(self, bord):
        if self.radius >= bord.radius + marginError:
            self.die(bord)

    def __str__(self):
        return str(self.score)

    def die(self, bord):
        self.score -= 5
        bord.radius = randint(bord.minRadius, bord.maxRadius)
        self.radius = 1
class rec(object):
    def __init__(self):
        self.x = 10
        self.y = 10
        self.width = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
        self.image = pygame.draw.rect(win, (255,255,255), self.rect)
    def draw(self):
        self.image = pygame.draw.rect(win, (255,255,255), self.rect)

a = rec()
def RedrawGameWindow(circ, bord):
    win.fill(0)
    circ.draw(win)
    text = font.render(str(circ), 1, (255, 255, 255))
    win.blit(text, (screen_width // 2 - text.get_width() // 2, 20))
    bord.draw(win)
    a.draw()
    pygame.display.update()


def main():
    running = True
    circ = circle()
    bord = border()
    while running:
        clock.tick(60)
        RedrawGameWindow(circ, bord)
        m = pygame.mouse.get_pressed()
        # if we check during the event for loop it won't check until
        # an event happens like a mouse position change or click
        circ.check(bord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                m = pygame.mouse.get_pressed()
                if m[0]:
                    circ.pop(bord)


main()
