import pygame
from random import randint
from time import time
pygame.init()
pygame.display.set_caption('Dino Game Definitely Didn\'t Steal From Google and Instagram Post')
screen_width = 500
screen_height = 500

font = pygame.font.SysFont('comicsans',200)
win = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()

class dino:
    def __init__(self,x,y,width,height,img=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.isJump = False
        self.score = 0
        self.isAlive = True
    def draw(self,window):
        self.move()
        if self.img:
            scale = pygame.transform.scale(self.img,(screen_width,screen_height))
            window.blit(scale)
        else:
            pygame.draw.rect(window,(0,0,0),(self.x,self.y,self.width,self.height))
    def move(self):
        pass
class obstacle:
    def __init__(self, x, y, width, height, img=None):
        self.x = x
        self.y = y
        self.yCopy = self.y
        self.width = width
        self.height = height
        self.heightCopy = self.height
        self.img = img
        self.shape = randint(1, 3)
        self.vel = 5
    def draw(self, window):
        self.move()
        if self.shape == 1:
            self.height = self.heightCopy
            self.y = self.yCopy
            pygame.draw.rect(window,(255,0,0),(self.x,self.y,self.width,self.height))
        elif self.shape == 2:
            self.height = self.heightCopy - 30
            self.y = self.yCopy - 20
            pygame.draw.rect(window,(0,255,0),(self.x,self.y,self.width,self.height))
        else:
            self.height = self.heightCopy
            self.y = self.yCopy
            pygame.draw.rect(window,(0,0,255),(self.x,self.y,self.width,self.height))

    def move(self):
        self.x -= self.vel
        if self.x + self.width + randint(0,30) < 0:
            self.shape = randint(1, 3)
            self.x = screen_width + randint(0,50)
din = dino(50,450,50,50)
obs1 = obstacle(300,450,50,50)
def RedrawGameWindow():
    win.fill((200,200,200))
    text = font.render(f'{din.score}', True,(0,0,0))
    # text.get_rect()[2] is width and text.get_rect()[3] is height
    # text.get_height() text.get_width()
    win.blit(text,(screen_width//2 - text.get_width()//2,screen_height//2 - text.get_height()//2))
    din.draw(win)
    obs1.draw(win)
    pygame.display.update()
velLoop = 5
jumpCount = 10
jumpLoop = 0
running = True
timeL = []
while running:
    RedrawGameWindow()
    clock.tick(60)
    currentTime = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    try:
        if din.isAlive and currentTime - timeL[-1] >= 0.5:
            din.score += 1
            timeL.append(time())
    except:
        timeL.append(time())
    if din.score % 10 == 0 and velLoop == 0 and din.score != 0:
        velLoop += 1
        obs1.vel += 0.1
    if velLoop > 0:
        velLoop += 1
    if velLoop > 10:
        velLoop = 0
    if jumpLoop > 0:
        jumpLoop += 1
    if jumpLoop > 6:
        jumpLoop = 0

    if key[pygame.K_SPACE]:
        din.isJump = True
    if din.isJump and jumpLoop == 0:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            din.y -= (jumpCount**2) * 0.2 * neg
            jumpCount -= 0.5
        else:
            jumpCount = 10
            din.isJump = False
            jumpLoop += 0.5
    if obs1.x <= din.x + din.width and obs1.x + obs1.width >= din.x:
        if din.y + din.height <= obs1.y + obs1.height and din.y + din.height >= obs1.y or din.y >= obs1.y and din.y <= obs1.y + obs1.height:
            print('b')
    if key[pygame.K_DOWN] and not(din.isJump):
        if din.height >= 20:
            din.height -= 5
            din.y += 5
    else:
        if din.height <= 45:
            din.height += 5
            din.y -= 5