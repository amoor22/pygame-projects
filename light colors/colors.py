import pygame

screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
green = (0, 255, 0)
red_ball = pygame.transform.scale(pygame.image.load('colors/red.png'), (600, 600))
other_ball = pygame.transform.scale(pygame.image.load('red.png'), (60, 60))
clock = pygame.time.Clock()
class ball:
    def __init__(self, x, y, img, color):
        self.x = x
        self.y = y
        self.image = img
        self.color = color
        self.mask = pygame.mask.from_surface(self.image)
        self.colliding_with = {}
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def collide(self, ball2):
        color = [0, 0, 0]
        for c in range(len(ball2.color)):
            color[c] += self.color[c]
            color[c] += ball2.color[c]
        result = self.mask.overlap_mask(ball2.mask, (ball2.x - self.x, ball2.y - self.y))
        result.to_surface(win, None, None, color, None, (self.x, self.y))
        self.colliding_with[ball2] = 1


def drawPix(color, x, y):
    win.fill(color, ((x, y), (5, 5)))


def RedrawGameWindow(balls):
    win.fill((255, 255, 255))
    for bll in balls:
        bll.draw(win)
    for b in balls:
        for bb in balls:
            b.colliding_with[bb] = 0
            try:
                if b is bb or b.colliding_with[bb] == 1:
                    continue
            except Exception as e:
                pass
            b.collide(bb)
    pygame.display.update()


def main():
    running = True
    balls = [ball(0, 0, red_ball, [255, 0, 0]), ball(50, 50, other_ball, [0, 255, 0]), ball(70, 70, other_ball, [0, 0, 255])]
    while running:
        clock.tick(60)
        RedrawGameWindow(balls)
        m = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        balls[1].x = mx - 30
        balls[1].y = my - 30
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()