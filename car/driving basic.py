import pygame
import math
pygame.init()
screen_width, screen_height = 800, 500
win = pygame.display.set_mode((screen_width, screen_height))
car_image = pygame.transform.scale(pygame.image.load('blue_car.png'), (50, 30))
race_track = pygame.transform.scale(pygame.image.load('track.png').convert(), (800, 500))
max_vel = 3
clock = pygame.time.Clock()
class car(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.image = pygame.transform.rotate(car_image, self.angle)
        self.vel = 0
        self.xvel = 0
        self.yvel = 0
        self.max_vel = 0
        self.color = (255, 0, 0)

    def draw(self, window):

        self.vel = self.lerp(self.vel, self.max_vel, 0.5)
        self.xvel = math.cos(math.radians(self.angle)) * self.vel
        # negative since positive y goes down and negative goes up
        self.yvel = -math.sin(math.radians(self.angle)) * self.vel

        self.x += self.xvel
        self.y += self.yvel
        window.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))

    def lerp(self, vel, g_vel, delta):
        difference = g_vel - vel
        if difference > delta:
            return vel + delta
        if difference < -delta:
            return vel - delta
        return g_vel


def RedrawGameWindow(new_car):
    win.blit(race_track, (0, 0))
    new_car.draw(win)
    pygame.display.update()


def main():
    running = True
    new_car = car(20, 20)
    loop = 0
    while running:
        clock.tick(60)
        RedrawGameWindow(new_car)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if loop > 0:
            loop += 1
        if loop > 15:
            loop = 0
        if key[pygame.K_w]:
            new_car.max_vel = max_vel
        elif key[pygame.K_s]:
            new_car.max_vel = -max_vel
        else:
            new_car.max_vel = 0
        if key[pygame.K_d]:
            print(new_car.angle)
            new_car.angle -= 3
            new_car.image = pygame.transform.rotate(car_image, new_car.angle)
        if key[pygame.K_a]:
            new_car.angle += 3
            new_car.image = pygame.transform.rotate(car_image, new_car.angle)


main()