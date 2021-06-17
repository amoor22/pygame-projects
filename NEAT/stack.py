import pygame
from random import randint,choice
pygame.init()
pygame.display.set_caption('Stacky Boi')
colors = [(167,15,205),
          (200,0,50),
          (0,210,0),
          (0,0,215),
          (15,179,205),
          (17,183,34)
          ]
screen_width = 500
screen_height = 500


font = pygame.font.SysFont('comicsans',30)
win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

class block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = -1
        self.vel = 5
        self.moving = True
        self.color = color
        self.hit = False
    def draw(self,window):
        if self.moving:
            self.move()
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.height))
    def move(self):
        self.x += self.vel * self.facing
        if self.x - 5 < 0:
            self.facing = 1
        elif self.x + self.width + 5 > screen_width:
            self.facing = -1
    def place(self):
        self.moving = False
        return True
    def checkCol(self,blocks):
        error = 7
        if self.x + self.width < blocks[-2].x:
            self.hit = True
        if not(self.moving) and self.x < blocks[-2].x:
            if not(self.moving) and self.x + error < blocks[-2].x:
                self.width -= abs(blocks[-2].x - self.x)
                self.x += blocks[-2].x - self.x
            else:
                self.x = blocks[-2].x
        elif not self.moving and self.x + self.width > blocks[-2].x + blocks[-2].width:
            if not self.moving and self.x + self.width - error > blocks[-2].x + blocks[-2].width:
                if abs((blocks[-2].x + blocks[-2].width) - (self.x + self.width)) > self.width:
                    self.hit = True
                else:
                    self.width -= abs((blocks[-2].x + blocks[-2].width) - (self.x + self.width))
            else:
                self.x -= abs((blocks[-2].x + blocks[-2].width) - (self.x + self.width))
        return self.width
def RedrawGameWindow(blocks,score,highScore):
    win.fill((0, 0, 0))
    text = font.render(f'score: {score}',True,(blocks[-1].color))
    win.blit(text, (20, 20))
    text2 = font.render(f'highscore: {highScore}',True,(blocks[-1].color))
    win.blit(text2, (200, 20))

    for blck in blocks:
        blck.draw(win)
    pygame.display.update()

def main():
    score = 0
    highScore = 0
    try:
        from high import highS
        highScore = highS
    except:
        with open('high.py','w') as file:
            file.write('highS = {}'.format(highScore))
            file.close()
    deleteAfter = randint(3,9)
    startY = screen_height - 80
    blocks = [block(screen_width//2 - 40,screen_height-40,80,40,choice(colors)),block(300,startY,80,40,choice(colors))]
    blocks[0].place()
    running = True
    spaceLoop = 0
    while running:
        clock.tick(60)
        RedrawGameWindow(blocks,score,highScore)
        if spaceLoop > 0:
            spaceLoop += 1
        if spaceLoop > 15:
            spaceLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if len(blocks) > deleteAfter:
            deleteAfter = randint(3,9)
            blocks.pop(0)
            for blck in blocks:
                blck.y += 40
        if keys[pygame.K_SPACE] and spaceLoop == 0:
            spaceLoop += 1
            blocks[-1].place()
            blocks[-1].checkCol(blocks)
            if not blocks[-1].hit:
                score += 1
            else:
                with open('high.py','w') as file:
                    if score > highScore:
                        file.write('highS = {}'.format(score))
                    else:
                        file.write('highS = {}'.format(highScore))
                    file.close()
                running = False
                pygame.quit()
                quit()
            startY = blocks[-1].y - 40
            blocks.append(block(randint(50,screen_width-50),startY,blocks[-1].checkCol(blocks),40,choice(colors)))

main()
