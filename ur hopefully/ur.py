import pygame
from random import randint
pygame.init()

screen_width = 900
screen_height = 700

win = pygame.display.set_mode((screen_width, screen_height))

board = pygame.image.load('board.png').convert()

clock = pygame.time.Clock()
class ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vel = 5
        self.color = (255, 0, 0)
        self.moves = 0
        self.pos = 0
        self.change = 0
        self.moving = True
        self.X = 0
        self.Y = 0
    def draw(self, window):
        self.move()
        pygame.draw.circle(window, (0,0,0), (self.x, self.y), self.r + 2)
        pygame.draw.circle(window, self.color, (self.x, self.y), self.r)
    def move(self):
        self.slide(self.X, self.Y)
        if self.moves >= 1:
            if not self.moving:
                if self.pos == 3:
                    self.moving = True
                    self.X = 0
                    self.Y = -1
                elif self.pos > 3:
                    self.moving = True
                    self.X = 1
                    self.Y = 0
                else:
                    self.moving = True
                    self.X = -1
                    self.Y = 0
                    print('dsa')
                self.moves -= 1
                self.pos += 1
    def slide(self, x, y):
        if self.moving:
            if self.change < 100:
                if self.change >= 90:
                    self.vel = 1
                self.x += self.vel * x
                self.y += self.vel * y
                self.change += self.vel
            else:
                self.moving = False
                self.change = 0
                self.vel = 5

class player:
    def __init__(self, startx,y):
        self.balls = []
        self.currentBall = None
        self.turn = False
        self.startx = startx
        self.y = y
        self.addballs()
    def addballs(self):
        for x in range(7):
            self.balls.append(ball(self.startx,self.y,10))
            self.startx += 50
    def move(self):
        if self.turn:
            self.balls[0].moves = 2
# add the list of balls to the player class
# then find a way to make him choose a ball to move
def RedrawGameWindow(balls,player1,player2):
    win.fill((0))
    win.blit(board,(screen_width//2 - board.get_width()//2,screen_height // 2 - board.get_height() // 2))
    for bll in player1.balls:
        bll.draw(win)
    for bal in player2.balls:
        bal.draw(win)
    for ball in balls:
        ball.draw(win)
    pygame.display.update()
# space from every block to the other is 100px
def main():
    running = True
    balls = [ball(400,450,10)]
    player1 = player(100,550)
    player1.turn = True
    player2 = player(100,125)
    while running:
        RedrawGameWindow(balls,player1, player2)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
main()