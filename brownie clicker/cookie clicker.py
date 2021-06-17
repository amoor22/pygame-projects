import pygame
from time import time
from random import randint

screen_width = 500
screen_height = 500

# gen
pygame.init()

win = pygame.display.set_mode((screen_width, screen_height))

buy_button_img = pygame.image.load('buy.png')

oven1 = pygame.image.load('oven1.png')
brownie_img = pygame.image.load('brownie.png')
brownie_bg = brownie_img.copy()
brownie_bg.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
clock = pygame.time.Clock()


class brownie:
    def __init__(self, img, x, y, width, height):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scaled = pygame.transform.scale(self.img, (self.width, self.height))
        self.score = 0

    def check_hover(self):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def draw(self, window):
        smaller = 10
        if small_loop == 0:
            self.scaled = pygame.transform.scale(self.img, (self.width, self.height))
            window.blit(self.scaled, (self.x, self.y))
        else:
            self.scaled = pygame.transform.scale(self.img, (self.width - smaller * 2, self.height - smaller * 2))
            window.blit(self.scaled, (self.x + smaller, self.y + smaller))


class backgroundC:
    def __init__(self):
        self.x = randint(0, screen_width)
        self.y = randint(-60, -20)
        self.wah = randint(20, 80)
        self.vel = (self.wah * 0.5) * 0.2
        self.aVel = 5

    def draw(self, window):
        self.move()
        self.aVel += 5
        scale = pygame.transform.scale(brownie_bg, (self.wah, self.wah))
        rotate = pygame.transform.rotate(scale, self.aVel)
        image_pos = (self.x - rotate.get_rect().width / 2,
                     self.y - rotate.get_rect().height / 2)
        window.blit(rotate, image_pos)

    def move(self):
        if self.y > screen_height:
            self.y = randint(-60, -20)
        self.y += self.vel
class buy_button:
    def __init__(self, x, y, width, height, pointsToBuy):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pointsToBuy = pointsToBuy
        self.bought = False
    def draw(self, window):
        # if not(self.bought):
            scale = pygame.transform.scale(buy_button_img,(self.width,self.height))
            window.blit(scale,(self.x,self.y))
    def checkHover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[0] > self.y and pos[1] < self.y + self.height:
                return True
        return False
class oven:
    def __init__(self,img, x,y, width, height, points, addevery):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = points
        self.addevery = addevery
        self.lastPointAddedTime = time()
    def draw(self, window):
        self.addPoints()
        scale = pygame.transform.scale(self.img,(self.width,self.height))
        window.blit(scale,(self.x, self.y))
    def addPoints(self):
        if current_time - self.lastPointAddedTime > self.addevery:
            self.lastPointAddedTime = time()
            brow.score += self.points


brow = brownie(brownie_img, screen_width // 2 - 75, screen_height // 2 - 75, 150, 150)
bs = []
ovn1 = oven(oven1,20,20,100,100,5,2)
buy1 = buy_button(25,25,64,64,10)
b = backgroundC()
small_loop = 0
pop_loop = 0

def RedrawGameWindow():
    win.fill((255, 255, 255))
    for x in bs:
        x.draw(win)
    brow.draw(win)
    if buy1.bought:
        ovn1.draw(win)
    buy1.draw(win)
    font = pygame.font.SysFont('comicsans', 200)
    score = font.render('{}'.format(brow.score), True, (255, 0, 0))
    win.blit(score, (screen_width // 2 - score.get_width() // 2, 20))
    pygame.display.update()


running = True
times = []
while running:
    current_time = time()
    clock.tick(60)
    RedrawGameWindow()
    if pop_loop > 0:
        pop_loop += 1
    if pop_loop > 10:
        pop_loop = 0
    if small_loop > 0:
        small_loop += 1
    if small_loop > 5:
        small_loop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pos = pygame.mouse.get_pos()
        if buy1.checkHover(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if brow.score >= buy1.pointsToBuy: # and not(buy1.bought)
                    brow.score -= buy1.pointsToBuy
                    buy1.bought = True
                    buy1.pointsToBuy += 10
        if brow.check_hover():
            if event.type == pygame.MOUSEBUTTONDOWN:
                times.append(time())
                if len(bs) < 75:
                    bs.append(backgroundC())
                brow.score += 1
                small_loop += 1
    try:# time now minus last click please understand
        # print(times[-1] - last)
        if current_time - times[-1] > 2:
            for x in bs:
                if x.y > screen_height - 10:
                    if pop_loop == 0: # we add the pop loop to space out the time between the disappearing of the brownies
                                      # since it would have to go from top to bottom again since the loop condition is not met (if == 0)
                        pop_loop += 1
                        bs.remove(x)
    except:
        pass