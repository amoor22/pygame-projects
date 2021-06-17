import pygame

pygame.init()
screen_width, screen_height = 560, 560
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
piece_colors = {"pawn": (0, 0, 255), "rook": (50, 50, 50), "knight": (255, 0, 0), "bishop": (255, 255, 0), "queen": (0, 255, 255), "king": (255, 0, 255)}

currently_showing = None

class board_piece:
    def __init__(self):
        self.row = None
        self.col = None
        self.piece = None
        self.show_move = False
        self.isBlack = None
        self.x = None
        self.y = None
        self.width = screen_width // 8

    def draw(self, x, y, isBlack):
        self.x = x
        self.y = y
        if isBlack:
            pygame.draw.rect(win, (0, 0, 0), (x, y, screen_width // 8, screen_height // 8))
        else:
            pygame.draw.rect(win, (255, 255, 255), (x, y, screen_width // 8, screen_height // 8))
        if self.show_move:
            pygame.draw.circle(win, (0, 255, 0), (x + (screen_width // 8) // 2, y + (screen_width // 8) // 2), 20)
        if self.piece:
            pygame.draw.rect(win, piece_colors[self.piece.type], (self.x + self.width // 4, self.y + self.width // 4, self.width // 2, self.width // 2))

    def click(self, pos):
        global currently_showing
        x, y = pos
        if self.x < x < self.x + self.width:
            if self.y < y < self.y + self.width:
                if self.show_move:
                    move_from_to(currently_showing, [self.row, self.col], board[currently_showing[0]][currently_showing[1]].piece)
                    renew_piece_pos()
                if self.piece:  # and (currently_showing == None or currently_showing == [self.row, self.col])
                    all_not_show()
                    for pos in self.piece.show_moves():
                        row, col = pos
                        if currently_showing == [self.row, self.col]:
                            board[row][col].show_move = False
                        else:
                            board[row][col].show_move = True
                    if currently_showing == [self.row, self.col]:
                        currently_showing = None
                    else:
                        currently_showing = [self.row, self.col]

def move_from_to(frm, to, piec):
    rowf, colf = frm
    rowt, colt = to
    board[rowf][colf].piece = None
    board[rowt][colt].piece = piec

board = [[board_piece() for i in range(8)] for j in range(8)]


def all_not_show():
    for row in range(len(board)):
        for col in range(len(board[0])):
            board[row][col].show_move = False
class piece:
    def __init__(self, row, col, type):
        self.row = row
        self.col = col
        self.type = type
def remove_negative(lst):
    rem = []
    for pos in range(len(lst)):
        row, col = lst[pos]
        if row < 0 or col < 0:
            rem.append(lst[pos])
    for i in rem:
        lst.remove(i)
class pawn(piece):
    def __init__(self, row, col):
        # piece.__init__(self, row, col)
        super().__init__(row, col, "pawn")
        self.first_move = True
    def show_moves(self):
        possible_moves = []
        if self.first_move:
            self.first_move = False
            if not board[self.row - 1][self.col].piece and self.row > 0:
                possible_moves.append([self.row - 1, self.col])
            if not board[self.row - 2][self.col].piece and self.row > 1:
                possible_moves.append([self.row - 2, self.col])
        else:
            if self.row > 0 and board[self.row - 1][self.col].piece is None:
                possible_moves.append([self.row - 1, self.col])
        return possible_moves
class rook(piece):
    def __init__(self, row, col):
        # piece.__init__(self, row, col, "rook")
        super().__init__(row, col, "rook")
    def show_moves(self):
        possible_moves = []
        for right in range(self.col + 1, len(board[0])):
            if board[self.row][right].piece is None:
                possible_moves.append([self.row, right])
            else: break
        for left in range(self.col - 1, -1, -1):
            if board[self.row][left].piece is None:
                possible_moves.append([self.row, left])
            else: break
        for up in range(self.row - 1, -1, -1):
            if board[up][self.col].piece is None:
                possible_moves.append([up, self.col])
            else: break
        for down in range(self.row + 1, len(board)):
            if board[down][self.col].piece is None:
                possible_moves.append([down, self.col])
            else: break
        return possible_moves
class knight(piece):
    def __init__(self, row, col):
        super().__init__(row, col, "knight")
    def show_moves(self):
        possible_moves = []
        try:
            if(board[self.row - 2][self.col + 1].piece is None):
                possible_moves.append([self.row - 2, self.col + 1])
        except IndexError: pass
        try:
            if(board[self.row - 2][self.col - 1].piece is None):
                possible_moves.append([self.row - 2, self.col - 1])
        except IndexError: pass
        try:
            if(board[self.row + 2][self.col + 1].piece is None):
                possible_moves.append([self.row + 2, self.col + 1])
        except IndexError: pass
        try:
            if(board[self.row + 2][self.col - 1].piece is None):
                possible_moves.append([self.row + 2, self.col - 1])
        except IndexError: pass
        try:
            if(board[self.row - 1][self.col + 2].piece is None):
                possible_moves.append([self.row - 1, self.col + 2])
        except IndexError: pass
        try:
            if(board[self.row + 1][self.col - 2].piece is None):
                possible_moves.append([self.row + 1, self.col - 2])
        except IndexError: pass
        try:
            if(board[self.row - 1][self.col - 2].piece is None):
                possible_moves.append([self.row - 1, self.col - 2])
        except IndexError: pass
        try:
            if(board[self.row + 1][self.col + 2].piece is None):
                possible_moves.append([self.row + 1, self.col + 2])
        except IndexError: pass
        remove_negative(possible_moves)
        return possible_moves
class bishop(piece):
    def __init__(self, row, col):
        super().__init__(row, col, "bishop")

    def show_moves(self):
        possible_moves = []
        rowC = self.row - 1
        for up_right in range(self.col + 1, len(board[0])):
            if board[rowC][up_right].piece is None:
                possible_moves.append([rowC, up_right])
            else: break
            rowC -= 1
        rowC = self.row - 1
        for up_left in range(self.col - 1, -1, -1):
            if board[rowC][up_left].piece is None:
                possible_moves.append([rowC, up_left])
            else: break
            rowC -= 1
        colC = self.col + 1
        for down_right in range(self.row + 1, len(board)):
            if down_right < len(board) and colC < len(board):
                if board[down_right][colC].piece is None:
                    possible_moves.append([down_right, colC])
                else: break
            colC += 1
        colC = self.col - 1
        for down_left in range(self.row + 1, len(board)):
            if board[down_left][colC].piece is None:
                possible_moves.append([down_left, colC])
            else: break
            colC -= 1
        remove_negative(possible_moves)
        return possible_moves
class queen(piece):
    def __init__(self, row, col):
        super().__init__(row, col, "queen")
    def show_moves(self):
        possible_moves = []
        rowC = self.row - 1
        for up_right in range(self.col + 1, len(board[0])):
            if board[rowC][up_right].piece is None:
                possible_moves.append([rowC, up_right])
            else: break
            rowC -= 1
        rowC = self.row - 1
        for up_left in range(self.col - 1, -1, -1):
            if board[rowC][up_left].piece is None:
                possible_moves.append([rowC, up_left])
            else: break
            rowC -= 1
        colC = self.col + 1
        for down_right in range(self.row + 1, len(board)):
            if down_right < len(board) and colC < len(board):
                if board[down_right][colC].piece is None:
                    possible_moves.append([down_right, colC])
                else: break
            colC += 1
        colC = self.col - 1
        for down_left in range(self.row + 1, len(board)):
            if board[down_left][colC].piece is None:
                possible_moves.append([down_left, colC])
            else: break
            colC -= 1
        for right in range(self.col + 1, len(board[0])):
            if board[self.row][right].piece is None:
                possible_moves.append([self.row, right])
            else: break
        for left in range(self.col - 1, -1, -1):
            if board[self.row][left].piece is None:
                possible_moves.append([self.row, left])
            else: break
        for up in range(self.row - 1, -1, -1):
            if board[up][self.col].piece is None:
                possible_moves.append([up, self.col])
            else: break
        for down in range(self.row + 1, len(board)):
            if board[down][self.col].piece is None:
                possible_moves.append([down, self.col])
            else: break
        remove_negative(possible_moves)
        return possible_moves
class king(piece):
    def __init__(self, row, col):
        super().__init__(row, col, "king")
    def show_moves(self):
        possible_moves = []
        if self.col < len(board) - 1:
            if board[self.row][self.col + 1].piece is None:
                possible_moves.append([self.row, self.col + 1])
            if self.row < len(board) - 1:
                if board[self.row + 1][self.col + 1].piece is None:
                    possible_moves.append([self.row + 1, self.col + 1])
            if self.row > 0:
                if board[self.row - 1][self.col + 1].piece is None:
                    possible_moves.append([self.row - 1, self.col + 1])
        if self.row < len(board) - 1:
            if board[self.row + 1][self.col].piece is None:
                possible_moves.append([self.row + 1, self.col])
            if self.col > 0:
                if board[self.row + 1][self.col - 1].piece is None:
                    possible_moves.append([self.row + 1, self.col - 1])
        if self.row > 0:
            if board[self.row - 1][self.col].piece is None:
                possible_moves.append([self.row - 1, self.col])
            if self.col > 0:
                if board[self.row - 1][self.col - 1].piece is None:
                    possible_moves.append([self.row - 1, self.col - 1])
        if self.col > 0:
            if board[self.row][self.col - 1].piece is None:
                possible_moves.append([self.row, self.col - 1])
        return possible_moves
board[7][0].piece = pawn(7, 0)
board[7][1].piece = rook(7, 1)
board[7][2].piece = knight(7, 2)
board[7][3].piece = bishop(7, 3)
board[7][4].piece = queen(7, 4)
board[7][5].piece = king(7, 5)
def renew_piece_pos():
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col].piece:
                board[row][col].piece.row = row
                board[row][col].piece.col = col

def draw_board():
    x = 0
    y = 0
    black = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            board[row][col].draw(x, y, black)
            board[row][col].row = row
            board[row][col].col = col
            x += screen_width // 8
            if black:
                black = False
            else:
                black = True
        if black:
            black = False
        else:
            black = True
        x = 0
        y += screen_height // 8


def RedrawGameWindow():
    win.fill(0)
    draw_board()
    pygame.display.update()

def main():
    running = True
    click_loop = 0
    while running:
        clock.tick(60)
        m = pygame.mouse.get_pressed()
        if m[0] and click_loop == 0:
            click_loop += 1
            for row in board:
                for b in row:
                    b.click(pygame.mouse.get_pos())
        RedrawGameWindow()
        if click_loop > 0:
            click_loop += 1
        if click_loop > 10:
            click_loop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
main()