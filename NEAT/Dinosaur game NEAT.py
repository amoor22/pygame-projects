import pygame
from random import randint
from time import time
import neat, os

pygame.init()
pygame.display.set_caption('Dino Game Definitely Didn\'t Steal From Google and Instagram Post')
screen_width = 500
screen_height = 500
GEN = 0
font = pygame.font.SysFont('comicsans', 20)
win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


class dino:
    def __init__(self, x, y, width, height, img=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.isJump = False
        self.isCrouch = False
        self.score = 0
        self.isAlive = True
        self.jumpLoop = 10
        self.jumpCount = 10
    def draw(self, window):
        self.move()
        if self.img:
            scale = pygame.transform.scale(self.img, (screen_width, screen_height))
            window.blit(scale)
        else:
            pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.width, self.height))

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
        self.color = None
        self.passing = False
    def draw(self, window):
        if self.shape == 1:
            self.height = self.heightCopy
            self.y = self.yCopy
            self.color = (255, 0, 0)
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        elif self.shape == 2:
            self.height = self.heightCopy #- 30
            self.y = self.yCopy #- 90
            self.color = (0, 255, 0)
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        else:
            self.height = self.heightCopy
            self.y = self.yCopy
            self.color = (0, 0, 255)
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self,dins=None):
        self.x -= self.vel
        if dins:
            for din in dins:
                if self.x + self.width < din.x:
                    print('dsa')
                    self.passing = True
                    self.shape = randint(1,3)
                else:
                    self.passing = False


def RedrawGameWindow(dins,obs,obs2,GEN):
    win.fill((200, 200, 200))
    text = font.render(f'{GEN}', True, (0, 0, 0))
    # text.get_rect()[2] is width and text.get_rect()[3] is height
    # text.get_height() text.get_width()
    win.blit(text, (10,10))
    for din in dins:
        din.draw(win)
    obs.draw(win)
    obs.move(dins)
    obs2.draw(win)
    obs2.move()
    pygame.display.update()

jumpCount = 10
jumpLoop = 0

def main(genomes, config):
    global GEN
    GEN += 1
    dins = []  #dino(50, 450, 50, 50)
    nets = []
    ge = []
    for _,g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g,config)
        nets.append(net)
        dins.append(dino(100, 450, 50, 50))
        g.fitness = 0
        ge.append(g)
    # dins.append(dino(100, 450, 50, 50))
    obs1 = obstacle(500, 450, 50, 50)
    obs2 = obstacle(500,450,50,50)
    obs2.shape = obs1.shape
    velLoop = 5
    running = True
    timeL = []
    rem = []
    while running:
        RedrawGameWindow(dins,obs1,obs2,GEN)
        clock.tick(60)
        currentTime = time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        for x,din in enumerate(dins):
            ge[x].fitness += 0.05
            output = nets[x].activate((din.y, abs(din.x - obs1.x),abs(din.y - obs1.y + obs1.height)))
            if output[0] > 0.5:
                din.isJump = True
            # else:
            #     din.isCrouch = True
        obs2.vel = obs1.vel
        if len(dins) <= 0:
            running = False
            break
        if obs1.passing:
            for g in ge:
                g.fitness += 5
            obs1.x = screen_width + randint(0,50)
        if obs2.x + obs2.width < 0:
            obs2.x = obs1.x
            obs2.shape = obs1.shape

        try:
            for din in dins:
                if din.isAlive and currentTime - timeL[-1] >= 0.5:
                    din.score += 1
                    timeL.append(time())
        except:
            timeL.append(time())

        if velLoop > 0:
            velLoop += 1
        if velLoop > 10:
            velLoop = 0
        # enumerate returns a tuple of the index and the object (0,bird) so we can pop it from other lists
        for x,din in enumerate(dins):
            if obs1.x <= din.x + din.width and obs1.x + obs1.width >= din.x:
                if din.y + din.height <= obs1.y + obs1.height and din.y + din.height >= obs1.y or din.y >= obs1.y and din.y <= obs1.y + obs1.height:
                    ge[x].fitness -= 2
                    dins.pop(x)
                    nets.pop(x)
                    ge.pop(x)

            if din.score % 10 == 0 and velLoop == 0 and din.score != 0:
                velLoop += 1
                obs1.vel += 0.1
            if din.jumpLoop > 0:
                din.jumpLoop += 1
            if din.jumpLoop > 10:
                din.jumpLoop = 0
            if din.isJump and din.jumpLoop == 0:
                try:
                    ge[x].fitness -= 2
                except:
                    print('c')
                if din.jumpCount >= -10:
                    neg = 1
                    if din.jumpCount < 0:
                        neg = -1
                    din.y -= (din.jumpCount ** 2) * 0.2 * neg
                    din.jumpCount -= 0.5
                else:
                    din.jumpCount = 10
                    din.isJump = False
                    din.jumpLoop += 0.5
            if din.isCrouch:
                if din.height >= 20:
                    din.height -= 5
                    din.y += 5
            else:
                if din.height <= 45:
                    din.height += 5
                    din.y -= 5


        # if key[pygame.K_SPACE]:
        #     din.isJump = True


def run(config_path):
    # setting up the config file P.s we add all titles in config except NEAT duh and we add the path
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    # setting the population
    p = neat.Population(config)
    # output
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # we chose the main function because the fitness is based
    # on how far they go through the level
    # so we would add to their fitness every frame
    winner = p.run(main,50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
