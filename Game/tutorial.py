import pygame

# initialize pygame
pygame.init()

# create window
screen_width = 500
screen_height = 450
win = pygame.display.set_mode((screen_width, screen_height))

# caption (title)
pygame.display.set_caption('Tutorial')

isJump = False
# pygame.image.load(pygame.path.join('folder','image')) or pygame.image.load('folder/image')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()
jumpCount = 10
x = 50
y = 450 - 64
height = 64
width = 64
vel = 5
running = True
left = False
right = False
walkCount = 0
def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1
    else:
        win.blit(char,(x,y))
while running:
    #pygame.time.delay(50)  # milliseconds
    clock.tick(27) # set fps
    redrawGameWindow()
    pygame.display.update()
    for event in pygame.event.get():  # get all events and check if they happened
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < (screen_width - vel - width):
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not isJump: # not isJump is True
        #if keys[pygame.K_UP] and y > vel:
            #y -= vel
        #if keys[pygame.K_DOWN] and y < screen_height - vel - height:
            #y += vel
        if keys[pygame.K_SPACE]:
            isJump = True # not isJump is now false
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10