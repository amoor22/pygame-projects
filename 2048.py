import pygame
import time
pygame.init()
screen_width = 500
screen_height = 500
font = pygame.font.SysFont('comicsans',30)
win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
class block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.color = (255,255,255)
        self.num = 2
        self.lastMove = time.time()
        self.moving = False
        self.CanMove = True
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
        number = font.render(f"{self.num}", 1, (0, 0, 0))
        window.blit(number, (self.x + (self.width // 2) - number.get_width()//2,
                             self.y + (self.width // 2) - number.get_height()//2))
    def move(self, blocks, keys):
        # it's comparing with itself+
        for blck in blocks:
            if blck != self:
                if self.x >= blck.x and self.x + self.width <= blck.x + blck.width:
                    if self.num == blck.num:
                        self.num += blck.num
                        blocks.remove(blck)
                        return True
        return False
    def checkRight(self, blocks):

        # check if it's exactly on top of it
        # now add stop if hit another block
        for blck in blocks:
            if blck != self:
                # if the block1 x plus width are bigger than block2 x
                # and block2 x smaller than block1 x plus it's width
                # and this is constrain and to avoid the statement triggering with blocks that are in the far right
                if self.x + self.width >= blck.x and blck.x <= self.x + self.width:
                    print('dsa')
                    if self.num != blck.num:
                        return False
                if self.x + self.width == blck.x + blck.width:
                    if self.num == blck.num:
                        blck.num += self.num
                        blocks.remove(self)
                    return False
        return True
    def checkLeft(self, blocks):
        for blck in blocks:
            if blck != self:
                if self.x <= blck.x + blck.width and blck.x +blck.width >= self.x:
                    blck.CanMove = False
                    self.CanMove = True
                if self.x == blck.x:
                    if self.num == blck.num:
                        blck.num += self.num
                        blocks.remove(self)
        return True
def moveAllBlocks(blocks, moving, tim):
    # don't know why any works, the player can't move until all blocks have moved
    # that was achieved by appending the moving of blocks (as true) if click
    # and checking if they are all not moving then the player can move again

    for blck in blocks:
        if keys[0]:
            blck.moving = True
            if not blck.x + blck.width >= screen_width and blck.checkRight(blocks):
                blck.x += 50
            else:
                blck.moving = False
        elif keys[1]:
            blck.moving = True
            if not blck.x <= 0 and blck.checkLeft(blocks) and blck.CanMove:
                blck.x -= 50
            else:
                blck.CanMove = True
                blck.moving = False
        elif keys[2]:
            blck.moving = True
            if not blck.y <= 0:
                blck.y -= 50
            else:
                blck.moving = False
        elif keys[3]:
            blck.moving = True
            if not blck.y + blck.width >= screen_height:
                blck.y += 50
            else:
                blck.moving = False
    moving.clear()
    for x in blocks:
        x.CanMove = True
        moving.append(x.moving)
    if not any(moving):
        keys[0] = 0
        keys[1] = 0
        keys[2] = 0
        keys[3] = 0
def RedrawGameWindow(blocks):
    win.fill(0)
    for bloc in blocks:
        bloc.draw(win)
    pygame.display.update()


keys = [0, 0, 0, 0]
def main():
    running = True
    blocks = [block(0, 0), block(450, 0), block(400, 0)]
    moving = []
    moveLoop = 0
    while running:
        clock.tick(15)
        if moveLoop > 0:
            moveLoop += 1
        if moveLoop > 5:
            moveLoop = 0
        current_time = time.time()
        moveAllBlocks(blocks, moving,current_time)
        RedrawGameWindow(blocks)
        key = pygame.key.get_pressed()
        # right - left - up - down
        for bloc in blocks:
            bloc.move(blocks, keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if moveLoop == 0:
            if not all(moving):
                if key[pygame.K_RIGHT]:
                    keys[0] = 1
                    moveLoop += 1
                elif key[pygame.K_LEFT]:
                    keys[1] = 1
                    moveLoop += 1
                elif key[pygame.K_UP]:
                    keys[2] = 1
                    moveLoop += 1
                elif key[pygame.K_DOWN]:
                    keys[3] = 1
                    moveLoop += 1


main()