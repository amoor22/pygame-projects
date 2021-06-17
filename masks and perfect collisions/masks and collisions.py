import pygame
pygame.init()

screen_width = 500
screen_height = 500

clock = pygame.time.Clock()

stkmn1 = pygame.image.load('stkmn1.png')
stkmask = pygame.mask.from_surface(stkmn1)

stkmn2 = pygame.image.load('stkmn2.png')

win = pygame.display.set_mode((screen_width, screen_height))


def RedrawGameWindow(particles):
    win.fill((128,0,0))
    scl = pygame.transform.scale(stkmn2,(500,500))
    scl_rect = scl.get_rect()
    stkmask2 = pygame.mask.from_surface(scl)
    mx, my = pygame.mouse.get_pos()
    x = screen_width // 2 - scl_rect.center[0]
    y = screen_width // 2 - scl_rect.center[1]
    offset = (mx - x, my - y)
    result = stkmask2.overlap(stkmask,offset)
    # offset = (x - mx, y -my)
    # result = stkmask.overlap(stkmask2,offset)
    if result:
        print('dsa')
    win.blit(scl, (x, y))
    win.blit(stkmn1, (mx, my))
    for particle in particles:
        particle.draw(win)
    pygame.display.update()

def main():
    running = True
    particles = []
    while running:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        RedrawGameWindow(particles)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()
