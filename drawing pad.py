import math
from PIL import Image
import numpy as np
import win32clipboard
from io import BytesIO
import pygame

pygame.init()

screen_width, screen_height, drawing_height = 500, 550, 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dot Thing")
clock = pygame.time.Clock()
block_num = 20
occ_grid, emp_grid = ".", " "
grid = [[" " for _ in range(block_num)] for _ in range(block_num)]
colors = {" ": (255, 255, 255), ".": (255, 0, 0)}

class block:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = screen_width // block_num
        self.text = None
        self.index = []
        self.colors = [(255, 255, 255), (255, 0, 0)]
        self.color_index = 0
        self.margin = 5
        self.clicked = False

    def draw(self, window, x, y, row, col):
        self.x, self.y = x, y
        self.index = [row, col]
        if self.clicked:
            self.color_index = 1
        else:
            self.color_index = 0
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.width))
        pygame.draw.rect(window, self.colors[self.color_index], (self.x, self.y, self.width, self.width))

    def click_old(self, pos):
        mx, my = pos
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.width:
                self.clicked = True
                row, col = self.index
                grid[row][col] = "."
    def unclick_old(self, pos):
        mx, my = pos
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.width:
                self.clicked = False
                row, col = self.index
                grid[row][col] = " "
    def click(self):
        row, col = self.index
        self.clicked = True
        grid[row][col] = occ_grid
    def unclick(self):
        row, col = self.index
        self.clicked = False
        grid[row][col] = emp_grid
class color:
    pass
def draw_blocks(win, blocks):
    x, y = 0, 0
    row, col = 0, 0
    width = screen_width // block_num
    for b in blocks:
        b.draw(win, x, y, row, col)
        x += width
        col += 1
        if col == block_num:
            col = 0
            row += 1
            x = 0
            y += width

def RedrawGameWindow(blocks):
    win.fill(0)
    draw_blocks(win, blocks)
    pygame.display.update()

def print_grid():
    string = ""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            string += grid[row][col]
        string += "\n"
    print(string)
def clear_grid(blocks):
    for blc in blocks:
        blc.clicked = False
        row, col = blc.index
        grid[row][col] = emp_grid
def from_row_col(row, col):
    return (row * block_num) + col
def export_image():
    data = np.empty((block_num, block_num, 3), dtype=np.uint8)
    for row in range(block_num):
        for col in range(block_num):
            data[row][col] = colors[grid[row][col]]
    img = Image.fromarray(data, "RGB")
    img.save(r"C:\Users\abdul\OneDrive\Desktop\ass.png")
    # Figure a way to resize without losing quality
    # Preferably a bigger canvas with a bigger brush
    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()

    filepath = r"C:\Users\abdul\OneDrive\Desktop\ass.png"
    image_ = Image.open(filepath)

    output = BytesIO()
    image_.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(win32clipboard.CF_DIB, data)
# export_image()
def main():
    running = True
    blocks = [block() for _ in range(block_num * block_num)]
    click_loop = 0
    while running:
        RedrawGameWindow(blocks)
        clock.tick(60)
        if click_loop > 0:
            click_loop += 1
        if click_loop > 20:
            click_loop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                col = math.floor(pygame.mouse.get_pos()[0]/(screen_width/block_num))
                row = math.floor(pygame.mouse.get_pos()[1]/(screen_width/block_num))
                if row < block_num and col < block_num:
                    blocks[from_row_col(row, col)].click()
                    current = from_row_col(row, col)
                    try:
                        blocks[from_row_col(row - 1, col)].click()
                        blocks[from_row_col(row + 1, col)].click()
                        if col != block_num - 1:
                            blocks[from_row_col(row, col + 1)].click()
                        if col != 0:
                            blocks[from_row_col(row, col - 1)].click()
                    except:
                        pass
                # for b in blocks:
                #     b.click(pygame.mouse.get_pos())
            elif mouse[2]:
                col = math.floor(pygame.mouse.get_pos()[0]/(screen_width/block_num))
                row = math.floor(pygame.mouse.get_pos()[1]/(screen_width/block_num))
                if row < block_num and col < block_num:
                    blocks[from_row_col(row, col)].unclick()
                # for b in blocks:
                #     b.unclick(pygame.mouse.get_pos())
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN] and click_loop == 0:
            click_loop += 1
            print_grid()
            export_image()
        elif key[pygame.K_BACKSPACE] and click_loop == 0:
            click_loop += 1
            clear_grid(blocks)

main()