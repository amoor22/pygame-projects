import pygame
from time import time
from itertools import groupby

pygame.init()

pygame.display.set_caption('Tetris Boi')
clock = pygame.time.Clock()
screen_width = 500
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))

class blockLine:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.widthC = self.width
        self.color = (255,255,255)
        self.blcks = []
        self.lastMoveT = []
        self.canMove = True
        self.moves = []
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x, self.y,self.width,self.height))
        pygame.draw.rect(window, self.color, (self.x + self.widthC * 1, self.y,self.width,self.height))
        pygame.draw.rect(window, self.color, (self.x + self.widthC * 2, self.y,self.width,self.height))
        pygame.draw.rect(window, self.color, (self.x + self.widthC * 3, self.y, self.width, self.height))
        self.blcks = [pygame.draw.rect(window,self.color,(self.x, self.y,self.width,self.height)),
                        pygame.draw.rect(window, self.color,(self.x + self.widthC * 1, self.y, self.width, self.height)),
                        pygame.draw.rect(window, self.color,(self.x + self.widthC * 2, self.y, self.width, self.height)),
                        pygame.draw.rect(window, self.color,(self.x + self.widthC * 3, self.y, self.width, self.height)),
                        pygame.draw.rect(window, self.color, (self.x + self.widthC * 4, self.y, self.width, self.height))
                      ]
    def move(self):
        if len(self.moves) == 0:
            self.y += 60
    def edgesR(self):
        for blck in self.blcks:
            if blck.x + blck.width + 50 > screen_width:
                return False
        return True
    def edgesL(self):
        for blck in self.blcks:
            if blck.x - 50 < 0:
                return False
        return True
    def checkStop(self,blocks):
        for blck in self.blcks:
            if blck.y + blck.height + 60 > screen_height:
                self.canMove = False
                return False
            for blc in blocks:
                print(len(blocks))
                # blck.x >= blc.x and blck.x + blck.width <= blc.x + blc.width
                if blck.y + blck.height >= blc.y and blck.x == blc.x:
                    self.canMove = False
                    return False
        return True

    def checkLine(self,blocks,draw):
        ys = []
        for blc in blocks:
            ys.append(blc.y)
        ys.sort()
        repeats = [len(list(group)) for key, group in groupby(ys)]
        new_ys = list(dict.fromkeys(ys))
        dic = dict(zip(new_ys,repeats))
        for y in dic:
            print(new_ys)
            print(dic)
            if dic[y] == 10:
                for blck in draw:
                    if not blck.canMove:
                        if blck.y == y:
                            draw.remove(blck)
                        for blc in blck.blcks:
                            if blc.y == y:
                                blck.blcks.remove(blc)

                for blck in draw:
                    diff = 0
                    if blck.y + blck.width <= y:
                        if diff == 0:
                            blck.y += 60
                        diff += 1
                dic[y] = 0
        dic.clear()
        new_ys.clear()
        repeats.clear()
        ys.clear()
class D(blockLine):
    def __init__(self,x,y,width,height):
        # Not using one of the following and adding a __init__ function means it will no longer inherit the __init__ function
        blockLine.__init__(self,x,y,width,height)
        # super().__init__(x,y,width,height) *** without self blz
def RedrawGameWindow(draw,blocks):
    win.fill((0,0,0))
    for blck in draw:
        blck.draw(win)
    # I don't know why but for some reason not clearing the list makes everything wrong
    if not draw[-1].canMove:
        blocks.clear()
        for blck in draw:
            for b in blck.blcks:
                blocks.append(b)
        draw.append(blockLine(0, 0, 50, 60))

    startX = 0
    startY = 0
    for _ in range(1,11):
        pygame.draw.line(win,(255,255,255),(startX,0),(startX,screen_height))
        startX += screen_width // 10
    for x in range(1,11):
        pygame.draw.line(win,(255,255,255),(0,startY),(screen_width,startY))
        startY += screen_height // 10
    pygame.display.update()
def main():
    running = True
    draw = [blockLine(0,0,50,60)]
    blocks = []
    if not(draw[-1].canMove):
        for block in draw:
            for blck in block.blcks:
                blocks.append(blck)
    while running:
        currrentTime = time()
        RedrawGameWindow(draw,blocks)
        clock.tick(60)
        # print(blocks)
        draw[-1].checkLine(blocks, draw)
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if key[pygame.K_RIGHT]:  # and draw[-1].x + (draw[-1].width * draw[-1].consist) + 50 <= screen_width:
                if draw[-1].edgesR() and draw[-1].canMove:
                    draw[-1].x += 50
            elif key[pygame.K_LEFT] and draw[-1].canMove:
                if draw[-1].edgesL():
                    draw[-1].x -= 50

        try:
            if currrentTime - draw[-1].lastMoveT[-1] > 0.2:
                if draw[-1].checkStop(blocks):
                    print(blocks)
                    draw[-1].y += 60
                    draw[-1].lastMoveT.append(time())
        except:
            draw[-1].lastMoveT.append(time())
main()