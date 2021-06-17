import pygame
# cookie clicker
pygame.init()

clock = pygame.time.Clock()

screen_width = 800
screen_height = 500

win = pygame.display.set_mode((screen_width,screen_height))

class rect:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xvel = 0
        self.xacc = 0
        self.yvel = 0
        self.yacc = 1
        self.collision_force = 0

    def draw(self, window):
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,self.width,self.height))
        self.x += self.xvel
        self.xvel += self.xacc
        self.collision_force = -self.xvel

        self.y += self.yvel
        self.yvel += self.yacc
new_rect = rect(200,200,30,50)

def RedrawGameWindow():
    win.fill((0,100,0))
    new_rect.draw(win)
    pygame.display.update()

running = True

while running:
    clock.tick(30)
    RedrawGameWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    # testing
    if new_rect.y + new_rect.width >= screen_height:
        new_rect.yvel *= -1
    if key[pygame.K_RIGHT]:
        new_rect.xacc += 0.05
    elif key[pygame.K_LEFT]:
        new_rect.xacc -= 0.05
    else:
        new_rect.xacc = 0
        new_rect.xvel *= 0.95
    if new_rect.x + new_rect.width + new_rect.xvel >= screen_width:
        # new_rect.xacc = 0
        new_rect.xvel -= 5
        new_rect.xacc = 0
        new_rect.xvel += new_rect.collision_force * 1.5
        # new_rect.x = screen_width - new_rect.width - 5
    elif new_rect.x - new_rect.xvel * 1.1 <= 0:
        new_rect.xvel += 5
        new_rect.xacc = 0
        new_rect.xvel += new_rect.collision_force * 1.5
    print(new_rect.xacc)

