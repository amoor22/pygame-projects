import pygame
# initialize pygame
pygame.init()

# create window
screen_width = 500
screen_height = 450
win = pygame.display.set_mode((screen_width, screen_height))
# text
font = pygame.font.Font('freesansbold.ttf', 30)
font_score = pygame.font.SysFont('comicsans', 30, True, True)  # True,True (bold,italic)
# audio and music
BulletSound = pygame.mixer.Sound('bullet.wav')
HitSound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)
# caption (title)
pygame.display.set_caption('Tutorial')

isJump = False
# pygame.image.load(pygame.path.join('folder','image')) or pygame.image.load('folder/image')
heart = pygame.image.load('broken123.png')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

score = 0

class player(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.jumpCount = 10
        self.walkCount = 0
        self.right = False
        self.left = False
        self.isJump = False
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11,29, 52)
        self.health = 100
        self.visible = True
    def draw(self,win):
        self.hitbox = (self.x + 17, self.y + 11,29, 52)

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.visible:
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            if not self.standing:
                if self.left:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                #win.blit(char, (self.x, self.y))
                if self.left:
                    win.blit(walkLeft[0],(self.x,self.y))
                else:
                    win.blit(walkRight[0],(self.x,self.y))
        else:
            pass
    def hit(self):
        print('bob ded')
        if self.health > 0:
            self.isJump = False
            self.jumpCount = 10
            self.health -= 5
            self.x = 50
            self.y = 381
            self.walkCount = 0
            i = 0
            while i < 200:
                pygame.time.delay(10)
                win.blit(heart,(screen_width/2 - 125,screen_height - 315))
                pygame.display.update()
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()
        else:
            self.visible = False


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2,31, 57)
        self.visible = True
        self.health = 50
    def draw(self,win):
        self.move()
        if self.visible:
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,50 - (50 - self.health),10))
            # pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,50 - (5 * (10 - self.health)),10)) or this if you set enemy health to 10 or 5 * self.health

            self.hitbox = (self.x + 17, self.y + 2,31, 57)
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel < 0:
                win.blit(self.walkLeft[self.walkCount // 3],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkRight[self.walkCount // 3],(self.x,self.y))
                self.walkCount += 1
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    def hit(self):
        if self.health > 0:
            self.health -= 5
            print('hit')
        else:
            self.visible = False
running = True
def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))
    bob.draw(win)
    goblin.draw(win)
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    text = font_score.render('score: {}'.format(score),1,(0,0,0))
    win.blit(text,(390,10))
    text = font.render('health: {}'.format(bob.health), True, (255, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    win.blit(text, textRect)
    for bullet in bullets:
        bullet.draw()

shootLoop = 0
healthLoop = 0
bullets = []#450-69
bob = player(50,381,64,64)
goblin = enemy(100,450-64,64,64,400)
while running:
    #pygame.time.delay(50)  # milliseconds
    clock.tick(27) # set fps
    redrawGameWindow()
    pygame.display.update()
    for event in pygame.event.get():  # get all events and check if they happened
        if event.type == pygame.QUIT:
            running = False
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 7:
        shootLoop = 0
    if healthLoop > 0 :
        healthLoop += 1
    if healthLoop > 20:
        healthLoop = 0
    # works but probably better
    if bob.visible:
        if bob.hitbox[0] + bob.hitbox[2] > goblin.hitbox[0] and bob.hitbox[0] + bob.hitbox[2] < goblin.hitbox[0] + goblin.hitbox[2] or bob.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2] and bob.hitbox[0] > goblin.hitbox[0]:
            if bob.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and bob.hitbox[1]  > goblin.hitbox[1] or bob.hitbox[1] + bob.hitbox[3] > goblin.hitbox[1] and bob.hitbox[1] + bob.hitbox[3] < goblin.hitbox[1] + goblin.hitbox[3]:
                if healthLoop == 0 and goblin.visible:
                    score -= 2
                    bob.hit()
                    healthLoop += 1
        for bullet in bullets:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and goblin.visible:
                    HitSound.play()
                    score += 1
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if bob.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(projectile(round(bob.x + bob.width // 2), round(bob.y + bob.height // 2), 7, (0, 0, 0),facing))
                BulletSound.play()

            shootLoop += 1
        if keys[pygame.K_LEFT] and bob.x > bob.vel:
            bob.x -= bob.vel
            bob.left = True
            bob.right = False
            bob.standing = False
        elif keys[pygame.K_RIGHT] and bob.x < (screen_width - bob.vel - bob.width):
            bob.x += bob.vel
            bob.right = True
            bob.left = False
            bob.standing = False
        else:
            #bob.right = False
            #bob.left = False
            bob.standing = True
            bob.walkCount = 0
        if not bob.isJump: # not isJump is True
            #if keys[pygame.K_UP] and bob.y > vel:
                #y -= bob.vel
            #if keys[pygame.K_DOWN] and bob.y < screen_height - vel - height:
                #y += vel
            if keys[pygame.K_UP]:
                bob.isJump = True  # not isJump is now false
                bob.right = False
                bob.left = False
                bob.walkCount = 0
        else:
            if bob.jumpCount >= -10:
                neg = 1
                if bob.jumpCount < 0:
                    neg = -1
                bob.y -= (bob.jumpCount ** 2) * 0.5 * neg
                bob.jumpCount -= 1
            else:
                bob.isJump = False
                bob.jumpCount = 10