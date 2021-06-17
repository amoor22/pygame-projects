import pygame
import math
pygame.init()

screen_width = 500
screen_height = 500

HW, HH = screen_width//2, screen_height//2

win = pygame.display.set_mode((screen_width, screen_height))
# we assign the x and y to middle of screen
x, y = HW, HH
# since there is no click at first the previous mouse x and y are set to x and y
pmx, pmy = x, y
clock = pygame.time.Clock()
speed = 5
# create a distance variable
distance = 0
running = True
while running:
    win.fill(0)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # checking for mouse press
    m = pygame.mouse.get_pressed()
    # not distance is true at first since there was no click
    # we there is distance this statement evaluates to false
    if m[0] and not distance:
        # getting mouse x and y
        mx, my = pygame.mouse.get_pos()
        # getting the distance from the mouse pos to the previous one
        # sqrt of (x2 - x1)^2 + (y2 - y1)^2 : which is the distance between two points formula
        distance = math.hypot(mx - pmx, pmy - my) / speed
        # we use int to remove decimal point so when we keep removing 1 from distance we don't run into problems
        distance = int(distance)
        # this line gets the angle between new and old mouse pos (tan-1)
        radians = math.atan2(my - pmy, mx - pmx)
        # we pretty much split the angle to dx and dy
        # dividing distance by speed and then multiplying dx and dy by it so the ball could go faster
        dx = math.cos(radians) * speed
        dy = math.sin(radians) * speed
        # since this part of code is not run when the ball is moving and only when the user clicks
        # we assign the previous mouse x and y pos to the new ones even before the ball reaches there because we already
        # have the distance and angle
        pmx, pmy = mx, my
    if distance:
        # if distance is not 0 we keep subtracting 1 until it is all the while we add the dx and dy
        # think of it like this we have a distance and we will change the x and y values of the ball
        # but the change in both might not be equal and this is why we get the angle between the 2 balls
        # and we break the angle into it's x and y components and therefore x might change more than y and vice versa
        distance -= 1
        x += dx
        y += dy
    if distance:
        # if the main ball hasn't reached the desired position draw a ball at the new mouse position
        pygame.draw.circle(win,(0,255,0),(pmx,pmy),5)
    # we use int so we don't run into problems with pygame
    pygame.draw.circle(win, (255,0,0), (int(x), int(y)),10)
    pygame.display.update()