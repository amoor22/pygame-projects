import pygame
from random import randint, random, choice
pygame.init()

oneorminus = [1,-1]

screen_width = 550
screen_height = 650

particles = []

clock = pygame.time.Clock()

win = pygame.display.set_mode((screen_width, screen_height))

stkmn1 = pygame.image.load('stkmn1.png')
stkmn2 = pygame.image.load('stkmn2.png')
sky = pygame.image.load('sky2.png').convert()

# move everything at a set velocity instead of at once and the player can't move during that
# gg boi
class particle:
    def __init__(self, x, y, width,color,xacc,yacc,facing, border=None):
        self.x = x
        self.y = y
        self.width = width
        self.border = border
        self.color = color
        self.yacc = yacc#-1
        self.yvel = 0
        self.xacc = xacc#0.5
        self.xvel = 0
        self.facing = facing
    def draw(self, window):
        self.yvel += self.yacc
        self.y += self.yvel

        self.xvel += self.xacc
        self.x += self.xvel
        if self.yvel > 0:
            self.width -= 0.5
        if self.facing == 1:
            if self.xacc < 0:
                self.xacc = 0
            else:
                self.xacc -= 0.04
        elif self.facing == -1:
            if self.xacc > 0:
                self.xacc = 0
            else:
                self.xacc += 0.04
        self.yacc += 0.06
        if self.border:
            pass
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width,self.width))
    def fillList(self,particles,num,x,y):
        particles.clear()
        for _ in range(num//2):
            particles.append(particle(x, y, 15, (255, 255, 255), random() * 0.9, -random(),1))
        for _ in range(num//2):
            particles.append(particle(x, y, 15, (255, 255, 255), -random() * 0.9, -random(),-1))
class background:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = self.y1 - screen_height
        self.vel = 5
        self.img = sky
        self.scaled = pygame.transform.scale(self.img,(screen_width,screen_height))
        self.rotated = pygame.transform.rotate(self.scaled,180)
    def draw(self):
        win.blit(self.scaled,(self.x1, self.y1))
        win.blit(self.rotated,(self.x2, self.y2))
    def move(self,stk):
        if not stk.CanJump or stk.top:
            self.y1 += self.vel
            self.y2 += self.vel
        # self.y1 = stk.y
        # self.y2 = self.y1 - screen_height
        if self.y1 >= screen_height:
            self.y1 = self.y2 - screen_height
        if self.y2 >= screen_height:
            self.y2 = self.y1 - screen_height

class platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100 # 60
        self.height = 30
        self.vel = 5
        self.yvel = 0
        self.facing = choice(oneorminus)
    def draw(self, window):
        self.move()
        pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.width, self.height))
    def move(self):
        self.y += self.yvel
        self.x += self.vel * self.facing
        if self.x + self.width + self.vel >= screen_width:
            self.facing *= -1
        if self.x - self.vel <= 0:
            self.facing *= -1
class man:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.jumpCount = 10
        self.img = stkmn1
        self.CanJump = True
        self.j = False
        self.form = 0
        self.ded = False
        self.top = False
    def draw(self, window):
        window.blit(self.img,(self.x,self.y))
    def jump(self):
        if self.CanJump:
            self.jumpCount = 10
            self.j = True
    def move(self, platforms):
        if self.jumpCount >= -10 and self.j:
            self.img = stkmn2
            self.CanJump = False
            neg = 1
            if self.jumpCount < 0:
                neg = -1
            d = (self.jumpCount ** 2) * 0.5 * neg
            self.y -= d
            self.jumpCount -= 1
        else:
            self.img = stkmn1
            self.CanJump = True
        if self.CanJump:
            self.x = platforms[self.form].x + platforms[self.form].width // 2 - self.img.get_width()//2
            self.y = platforms[self.form].y - self.img.get_height()
            if self.form >= 4:
                self.top = True
            if self.form >= 1 and self.top:
                self.CanJump = False
                for form in platforms:
                    form.yvel = 5
                    if form.y >= screen_height:
                        platforms.remove(form)
                        platforms.append(platform(100,platforms[-1].y - 100))
                        self.form -= 1
                print(self.form)
            else:
                self.CanJump = True
                for form in platforms:
                    form.yvel = 0
                self.top = False
        else:
            if d < 0:
                if self.y >= platforms[self.form + 1].y:
                    if self.x + self.img.get_width() >= platforms[self.form + 1].x and self.x <= platforms[self.form + 1].x + platforms[self.form + 1].width:
                        particle.fillList(clock, particles, 29, self.x, self.y)
                        self.form += 1
                        self.jumpCount = -11
                        self.CanJump = True
                    else:
                        if self.x + self.img.get_width() >= platforms[self.form].x and self.x <= platforms[
                            self.form].x + platforms[self.form].width:
                            particle.fillList(clock, particles, 29, self.x, self.y)
                        else:
                            self.form = 0
b = background()
def RedrawGameWindow(particles,stk,platforms):
    win.fill((0,0,0))
    b.draw()
    b.move(stk)
    stk.draw(win)
    for platform in platforms:
        platform.draw(win)
    for particle in particles:
        particle.draw(win)
    pygame.display.update()

def main():
    running = True
    platforms = [platform(250,600),platform(200,500),platform(150,400),platform(100,300),platform(320,200)]
    stk = man(40, platforms[0].y - stkmn1.get_height())
    while running:
        clock.tick(60)
        RedrawGameWindow(particles,stk,platforms)
        stk.move(platforms)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                stk.jump()

main()
