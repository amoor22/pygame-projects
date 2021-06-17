import pygame
from random import randint
pygame.init()
pygame.display.set_caption('Bing-Bong')

score_sound = pygame.mixer.Sound('score.wav')
pts_10_sound = pygame.mixer.Sound('10pts.wav')

screen_width = 500
screen_height = 500

font = pygame.font.SysFont('comicsans', 50, True, True)

win = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()

running = True
class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.jumpCount = 10
        self.facing = 1
        self.isJump = False
        self.score = 0
    def draw(self,window):
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,self.width,self.height))
class computer(player):
    # or pass
    def __init__(self,x,y,width,height):
        player.__init__(self,x,y,width,height)
        self.hitEdge = False
        # or super().__init__(x,y,width,height)
    def draw(self,window):
        self.move()
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,self.width,self.height))
    def move(self):
        if new_ball.x > self.x and not(self.hitEdge) and not(new_ball.OutOfBounds):
            self.x += self.vel
        elif new_ball.x < self.x + (self.width // 2) and not(self.hitEdge) and not(new_ball.OutOfBounds):
            self.x -= self.vel
        if self.x + self.width + self.vel >= screen_width:
            self.hitEdge = True
            self.x -= self.vel
        elif self.x <= 0:
            self.hitEdge = True
            self.x += self.vel
        else:
            self.hitEdge = False

class ball:
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel = 10
        self.bounce = False
        self.facing = 1
        self.OutOfBounds = False
    def move(self):
        self.x -= self.vel * self.facing
        if self.y + self.radius > wall.y + wall.height and self.y - self.radius < wall.y + wall.height and self.x + self.radius > wall.x and self.x - self.radius < wall.x + wall.width:
            self.bounce = True
            score_sound.play()
        if self.y + self.radius >= player1.y and self.x + self.radius > player1.x and self.x - self.radius < player1.x + player1.width and self.y < player1.y:
            self.bounce = False
            player1.score += 1
            if player1.score % 5 == 0:
                pts_10_sound.play()
            else:
                score_sound.play()
        if self.y < (wall.y + wall.height) - 5 or self.y > player1.y + 5:
            self.OutOfBounds = True
        if self.bounce:
            self.y += self.vel
        else:
            self.y -= self.vel
        if self.x + self.radius >= screen_width:
            self.facing = 1
        elif self.x - self.radius < 0:
            self.facing = -1
    def draw(self,window):
        self.move()
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)

wall = computer(20,20,100,30)
player1 = player(20,450,100,30)
new_ball = ball(randint(20,450),randint(50,400),(0,255,0),20)

def RedrawGameWindow():
    win.fill((0, 0, 0))
    score = font.render('{}'.format(player1.score),1,(90,90,90))
    win.blit(score,(screen_width//2 - score.get_width(),screen_height//2 - score.get_height()))
    player1.draw(win)
    wall.draw(win)
    new_ball.draw(win)
    pygame.display.update()
while running:
    clock.tick(27)
    RedrawGameWindow()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player1.x + player1.width + player1.vel < screen_width:
        player1.x += player1.vel
        player1.facing += 1
    elif keys[pygame.K_LEFT] and player1.x - player1.vel > 0:
        player1.x -= player1.vel
        player1.facing -= 1
    else:
        player1.facing = 0


