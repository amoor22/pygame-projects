import pygame
import math
from math import sin, cos, radians

pool1 = pygame.image.load(r'pool/pool1.png')
pool2 = pygame.image.load(r'pool/pool2.png')
pool3 = pygame.image.load(r'pool/pool3.png')
pool4 = pygame.image.load(r'pool/pool4.png')
pool5 = pygame.image.load(r'pool/pool5.png')
pool6 = pygame.image.load(r'pool/pool6.png')
pool7 = pygame.image.load(r'pool/pool7.png')
pool8 = pygame.image.load(r'pool/pool8.png')

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Billiards Pendulum')
pygame.display.set_icon(pool1)

screen_width = 700
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))

running = True


class pendulum:
    def __init__(self, x1, y1, len, angle, image):
        self.x1 = x1
        self.y1 = y1
        self.len = len
        self.angle = radians(angle)
        self.ball_x = self.x1 + sin(self.angle) * self.len
        self.ball_y = self.y1 + cos(self.angle) * self.len
        self.aVel = 0
        self.aAcc = 0
        self.gravity = 1
        self.image = image

    def draw(self, window):
        self.ball_x = self.x1 + sin(self.angle) * self.len
        self.ball_y = self.y1 + cos(self.angle) * self.len
        # * by 0.5 optional
        self.aAcc = (-1 * self.gravity / (self.len * 0.5)) * sin(self.angle)
        self.aAcc *= 0.999
        self.aVel += self.aAcc
        self.angle += self.aVel
        pygame.draw.line(window, (255, 255, 255), (self.x1, self.y1), (self.ball_x, self.ball_y), 10)
        # pygame.draw.circle(window, (255, 255, 255), (int(self.ball_x), int(self.ball_y)), 30)
        new_image = pygame.transform.scale(self.image, (60, 60))
        window.blit(new_image,
                    (int(self.ball_x - new_image.get_width() // 2), int(self.ball_y - new_image.get_height() // 2)))


# new_pendulum1 = pendulum(screen_width // 2, -5, 300, 50, pool3)
# new_pendulum2 = pendulum(screen_width // 2, -5, 275, 50, pool2)
# new_pendulum3 = pendulum(screen_width // 2, -5, 250, 50, pool1)
# new_pendulum4 = pendulum(screen_width // 2, -5, 250, 50, pool1)
# new_pendulum5 = pendulum(screen_width // 2, -5, 250, 50, pool1)
# new_pendulum6 = pendulum(screen_width // 2, -5, 250, 50, pool1)
# new_pendulum7 = pendulum(screen_width // 2, -5, 250, 50, pool1)
# new_pendulum8 = pendulum(screen_width // 2, -5, 250, 50, pool1)
# new_pendulum9 = pendulum(screen_width // 2, -5, 250, 50, pool1)

balls = [pendulum(screen_width // 2, -5, 400, 50, pool8),
         pendulum(screen_width // 2, -5, 375, 50, pool7),
         pendulum(screen_width // 2, -5, 350, 50, pool6),
         pendulum(screen_width // 2, -5, 325, 50, pool5),
         pendulum(screen_width // 2, -5, 300, 50, pool4),
         pendulum(screen_width // 2, -5, 275, 50, pool3),
         pendulum(screen_width // 2, -5, 250, 50, pool2),
         pendulum(screen_width // 2, -5, 225, 50, pool1),
         ]

num = 8
num = 8 - num

def RedrawGameWindow():
    global num
    win.fill((0, 140, 51))
    for rem in range(num):
        print(rem)
        balls.pop(0)
    num = 0
    for ball in balls:
        ball.draw(win)
    # new_pendulum1.draw(win,pool1)
    pygame.display.update()


while running:
    RedrawGameWindow()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
