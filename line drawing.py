import pygame

pygame.init()

screen_width, screen_height = 500, 500

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = (255, 255, 255)
def RedrawGameWindow(points, list_index):
    win.fill(0)
    for j in range(0, len(points)):
        for i in range(0, len(points[j]) - 1):
            x1, y1 = points[j][i]
            x2, y2 = points[j][i + 1]
            pygame.draw.line(win, (255, 255, 100), (x1, y1), (x2, y2))
    pygame.display.update()

def main():
    running = True
    points = [[]]
    list_index = 0
    loop = 0
    while running:
        clock.tick(60)
        RedrawGameWindow(points, list_index)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if loop > 0:
            loop += 1
        if loop > 10:
            loop = 0
        m = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if m[0] and loop == 0:
            loop += 1
            points[list_index].append(pos)
        if m[2] and loop == 0:
            loop += 1
            points.append([])
            list_index += 1

main()