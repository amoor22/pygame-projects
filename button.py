import pygame
# gen
pygame.init()
clock = pygame.time.Clock()

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width,screen_height))
# text='' and outline=None indicate that it is not necessary to have them in an instance but if filled they would be there
class button:
    def __init__(self, colour, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
    def draw(self, window, outline=None,thicc=None):
        if outline:
            pygame.draw.rect(window, outline, (self.x - thicc, self.y - thicc, self.width + thicc * 2, self.height + thicc * 2))
        pygame.draw.rect(window,self.colour,(self.x,self.y,self.width,self.height))
        if self.text != '':
            pygame.font.init()
            font = pygame.font.SysFont('comicsans',20)
            text = font.render(self.text,1,(0,0,0))
            win.blit(text,(self.x + (self.width //2 - text.get_width()//2),self.y + (self.height//2 - text.get_height()//2)))

    def check_hover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
rec = button((0,0,255),250 - 70,250 - 70,100,70,'Button')

def RedrawGameWindow():
    win.fill((255,255,255))
    rec.draw(win,(255,0,0),3)

    pygame.display.update()

running = True

while running:
    RedrawGameWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pos = pygame.mouse.get_pos()
        old_color = (0,0,255)
        new_color = (0,255,0)
        if rec.check_hover(pos):
            rec.colour = new_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('b')
        else:
            rec.colour = old_color
