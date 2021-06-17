import pygame

pygame.init()
broken = []
screen_width, screen_height = 560, 560

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


class brick:
    def __init__(self):
        self.x = None
        self.y = None
        self.X = None
        self.Y = None
        self.width = 70
        self.height = 30
        self.margin = 5
        self.Width = self.width - self.margin
        self.Height = self.height - self.margin
        self.color = (255, 255, 255)
        self.index = 0

    def draw(self, window, x, y):
        self.x = x
        self.y = y
        self.X = self.x + self.margin
        self.Y = self.y + self.margin
        pygame.draw.rect(window, self.color, (self.x + self.margin, self.y + self.margin, self.width - self.margin - self.margin, self.height - self.margin - self.margin))


def draw_bricks(bricks):
    x = 0
    y = 100
    for i, bric in enumerate(bricks):
        if i not in broken:
            bric.draw(win, x, y)
        bric.index = i
        if (i + 1) % 8 == 0 and i != 0:
            y += bric.height
            x = 0
        else:
            x += bric.width

class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = (255, 255, 0)
        self.xvel = 5
        self.yvel = -5

    def draw(self, window, bricks, new_bat):
        self.move()
        self.check_collision(bricks, new_bat)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.xvel
        self.y += self.yvel

    def check_collision(self, bricks, new_bat):
        if self.y - self.radius <= 0:
            self.yvel *= -1
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.xvel *= -1
        if self.x + self.radius > new_bat.x and self.x - self.radius < new_bat.x + new_bat.width:
            if self.y + self.radius > new_bat.y and self.y + self.radius < new_bat.y + new_bat.height:
                if new_bat.positions[-1] - new_bat.positions[-2] > 0:
                    if self.xvel < 0:
                        self.xvel *= -1
                else:
                    if self.xvel > 0:
                        self.xvel *= -1
                self.yvel *= -1
        for i, bric in enumerate(bricks):
            if self.x + self.radius > bric.X and self.x - self.radius < bric.X + bric.Width:
                if self.y - self.radius < bric.Y + bric.Height and self.y + self.radius > bric.Y:
                    if i not in broken:
                        self.xvel *= -1
                        self.yvel *= -1
                        broken.append(i)
                    # bricks.remove(bric)
class bat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 175
        self.height = 20
        self.middle = 0
        self.positions = [0, 0]
    def draw(self, window, pos):
        x, y = pos
        self.x = x - self.width // 2
        self.positions.pop(0)
        self.positions.append(self.x)
        self.middle = x
        pygame.draw.rect(window, (255, 0, 255), (self.x, self.y, self.width, self.height))


def RedrawGameWindow(bricks, new_ball, new_bat):
    win.fill(0)
    draw_bricks(bricks)
    new_ball.draw(win, bricks, new_bat)
    pos = pygame.mouse.get_pos()
    new_bat.draw(win, pos)
    pygame.display.update()


def main():
    running = True
    bricks = [brick() for _ in range(40)]
    new_ball = ball(screen_width // 2, 300)
    new_bat = bat(10, screen_height - 50)
    while running:
        RedrawGameWindow(bricks, new_ball, new_bat)
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()