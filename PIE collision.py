import pygame

pygame.init()

screen_width = 1000
screen_height = 500

win = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
class rect:
    def __init__(self,x,y,width,mass,facing):
        self.x = x
        self.y = y
        self.width = width
        self.mass = mass
        self.facing = facing
        self.vel = 0
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255),(self.x,self.y,self.width,self.width))

rect1 = rect(220, 400,40,1000,-1)
rect2 = rect(150,410,30,1,-1)
rect1.vel = 3
print(rect1.vel)
def RedrawGameWindow():
    win.fill((0,0,0))
    rect1.draw(win)
    rect2.draw(win)
    pygame.display.update()
num = -1
def CheckCollision():
    global num
    if rect2.x + rect2.width >= rect1.x:
        print('b')
        num += 1
        rect1.vel -= abs(rect2.vel) * rect2.mass
        rect2.vel += (rect1.vel * rect1.mass) * 0.001
        print(rect2.vel)

    if rect2.x <= 0:
        num += 1
        rect2.facing = -rect2.facing
    rect1.x -= rect1.vel
    rect2.x += rect2.vel * rect2.facing
running = True
while running:
    RedrawGameWindow()
    CheckCollision()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(num)
            running = False