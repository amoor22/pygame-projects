import pygame
import neat

pygame.init()
pygame.display.set_caption('Flappy Boi')
screen_width = 500
screen_height = 700

win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
class flapp:
    def __init__(self,x,y,width,height):
        pass

def RedrawGameWindow():
    win.fill((255,255,255))
    pygame.display.update()

def main():
    running = True
    while running:

        clock.tick(60)
        RedrawGameWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

main()