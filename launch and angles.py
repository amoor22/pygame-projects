import pygame
import math

pygame.init()
screen_width, screen_height = 1080, 650
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
gravity = 2
class dynamic_ball(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.xvel = 0
        self.xacc = 0
        self.yvel = 0
        self.yacc = 0
        self.max_vel = 15
        self.color = (255, 0, 0)
    def draw(self, window, mousepos):
        self.move()
        mx, my = mousepos
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.line(window, self.color, (self.x, self.y), (mx, my))
    def move(self):
        self.yacc += 0.1
        # if self.xvel + self.xacc >= self.max_vel:
        #     self.xvel = self.max_vel
        # if self.yvel + self.yacc >= self.max_vel:
        #     self.yvel = self.max_vel
        #
        # if self.xvel + self.xacc <= -self.max_vel:
        #     self.xvel = -self.max_vel
        # if self.yvel + self.yacc <= -self.max_vel:
        #     self.yvel = -self.max_vel
        self.xvel *= .90
        self.yvel *= .90
        self.xvel += self.xacc
        self.yvel += self.yacc
        if self.y + self.radius + self.yvel > screen_height:
            # we reverse the direction of the ball and halve it
            # and we halve the acceleration without changing the direction
            self.yvel *= -0.5
            self.yacc *= 0.5
        if self.x + self.radius + self.yvel > screen_width:
            # we reverse the direction of the ball and halve it
            # and we halve the acceleration without changing the direction
            self.xvel *= -0.5
            # we deduct from the x to stop it from being stuck
            self.x -= 5
            self.xacc *= 0.5
        self.x += self.xvel
        self.y += self.yvel

    def launch(self, mousepos):
        mx, my = mousepos
        # self.x = self.radius
        # self.y = screen_height - self.radius - 10
        self.xacc, self.yacc, self.xvel, self.yvel = 0, 0, 0, 0
        angle = math.atan2(my - self.y, mx - self.x)
        power = math.hypot(mx - self.x, my - self.y) * 0.01
        self.yacc = math.sin(angle) * power
        self.xacc = math.cos(angle) * power
def RedrawGameWindow(ball, pos):
    win.fill(0)
    ball.draw(win, pos)
    pygame.display.update()
def main():
    running = True
    new_ball = dynamic_ball(0, screen_height - 20 - 10, 20)
    click_loop = 0
    while running:
        pos = pygame.mouse.get_pos()
        RedrawGameWindow(new_ball, pos)
        clock.tick(60)
        if click_loop > 0:
            click_loop += 1
        if click_loop > 20:
            click_loop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            m = pygame.mouse.get_pressed()
            if m[0] and click_loop == 0:
                click_loop += 1
                pos = pygame.mouse.get_pos()
                new_ball.launch(pos)

        key = pygame.key.get_pressed()
main()