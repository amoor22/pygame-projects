import pygame
from math import atan2,atan
pygame.init()

screen_width = 500
screen_height = 500

clock = pygame.time.Clock()
win = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Projectile motion')

rect = pygame.image.load('get_rect.png')
pygame.transform.rotate(win, -20)

running = True

class cannon:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
    def draw(self,window):
        global image_pos
        mouse_pos = pygame.mouse.get_pos()
        scaled = pygame.transform.scale(self.image, (100, 20))
        angle = atan2(mouse_pos[1] - self.y,mouse_pos[0] - self.x)
        rotated = pygame.transform.rotate(scaled,360 - angle * 57.29)
        image_pos = (self.x - rotated.get_rect().width/2,
                     self.y - rotated.get_rect().height/2)
        window.blit(rotated, image_pos)
class projectile():
    def __init__(self, radius, colour, x, y):
        self.radius = radius
        self.colour = colour
        self.x = x
        self.y = y
        self.vel = 3
        self.OnGround = True
        self.jump = False
        self.springingaction = self.vel
    def move(self):
        if self.y + self.radius< screen_height and not(self.jump):
            self.y += self.vel
            self.vel = int(self.vel + (7 ** 2) *0.04)
            print(self.vel)
            self.OnGround = False
        else:
            self.y -= self.springingaction
            #if not self.jump:
                #self.y = screen_height - self.radius
            self.OnGround = True
    def draw(self,window):
        global image_pos
        self.move()
        #pygame.draw.circle(window,self.colour,(int(image_pos[0]),int(image_pos[1])),self.radius)
        pygame.draw.circle(window,self.colour,(self.x,self.y),self.radius)

new_cannon = cannon(rect,100,100)
ball = projectile(10,(255,0,0),screen_width//2,screen_width//2)
def RedrawGameWindow():
    win.fill((0,0,0))
    new_cannon.draw(win)
    ball.draw(win)
    pygame.display.update()
while running:
    clock.tick(27)
    RedrawGameWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball.OnGround:
        ball.jump = True
        ball.y -= 7
    else:
        ball.jump = False
