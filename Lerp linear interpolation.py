import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 500
win = pygame.display.set_mode((screen_width, screen_width))
class block:
    def __init__(self):
        self.x = 0
        self.y = 100
        self.width = 70
        self.height = 30
        self.vel = 0
        self.Gvel = 0
        self.color = (255, 255, 0)
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
    def move(self):
        self.vel = self.lerp(self.vel, self.Gvel, 0.5)
        self.x += self.vel

    def lerp(self, vel, Gvel, dt):
        difference = Gvel - vel
        if difference > dt:
            return vel + dt
        if difference < -dt:
            # -15 < -0.1
            # -0.1
            return vel - dt
        return Gvel
def RedrawGameWindow(car):
    win.fill(0)
    car.draw(win)
    car.move()
    pygame.display.update()


def main():
    running = True
    car = block()
    while running:
        RedrawGameWindow(car)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            car.Gvel = 10
        elif key[pygame.K_LEFT]:
            car.Gvel = -10
        else:
            car.Gvel = 0
main()