import pygame
from random import randint,choice
from time import time
import neat, os
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
def RedrawGameWindow(blocks):
    win.fill((0, 0, 0))
    for blck in blocks:
        blck.draw(win)
    pygame.display.update()

def main(genomes, config):
    strtTime = time()
    spaceLoop = 0
    startY = screen_height - 80
    nets = []
    ge = []
    blocks = [block(250,screen_height-40,80,40,choice(colors)),block(250,startY,80,40,choice(colors))]
    for _,g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g,config)
        nets.append(net)
        # blocks.append(block(250,screen_height-40,80,40,choice(colors)),block(250,startY,80,40,choice(colors)))
        g.fitness = 0
        ge.append(g)
    deleteAfter = randint(3,9)
    blocks[0].place()
    running = True
    while running:
        current_time = time()
        clock.tick(60)
        RedrawGameWindow(blocks)

        for y, blck in enumerate(blocks):
            if abs(blck.width) > 80:
                for g in ge:
                    g.fitness -= 5
                running = False
            output = nets[y].activate((blocks[-1].x,
                                       abs(blocks[-1].x - blocks[-2].x),
                                       abs((blocks[-1].x + blocks[-1].width) - (blocks[-2].x + blocks[-2].width))))
            if output[0] > 0.5 and spaceLoop == 0:
                print('v')
                blocks[-1].checkCol(blocks)
                startY = blocks[-1].y - 40
                blocks[-1].place()
                blocks.append(block(randint(50, screen_width - 50), startY, blocks[-1].checkCol(blocks), 40, choice(colors)))
                spaceLoop += 1
        for g in ge:
            if blocks[-1].hit or current_time - strtTime > 3:
                g.fitness -= 3

                running = False
            try:
                if not blocks[-1].moving:
                    strtTime = time()
                    g.fitness += blocks[-1].width * 0.5
            except:
                pass
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

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    # population
    p = neat.Population(config)
    # output
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'config-feedforward.txt')
    run(config_path)