import pygame
pygame.init()

screen_width, screen_height = 600, 600

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
scores = {'x': 1, 'o': -1, 'tie': 0}
can_play = True
class box:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = 200
        self.symbol = ''
        self.color = (255, 255, 255)
        self.margin = 10
        self.index = [0, 0]
        self.num = 0
        self.clicked = False

    def draw(self, window, x, y):
        self.x = x
        self.y = y
        row, col = self.index
        pygame.draw.rect(window, (255, 0, 0), (x, y, self.width, self.width))
        if board[row][col] == 'x':
            pygame.draw.line(window, self.color, (x + self.margin, y + self.margin), (x + self.width - self.margin, y + self.width - self.margin), 10)
            pygame.draw.line(window, self.color, (x + self.width - self.margin, y + self.margin), (x + self.margin, y + self.width - self.margin), 10)
        elif board[row][col] == 'o':
            pygame.draw.circle(window, self.color, (self.x + (self.width // 2), self.y + (self.width // 2)), (self.width // 2) - self.margin, 10)

    def click(self, pos, turns):
        mx, my = pos
        row, col = self.index
        if not self.clicked:
            if self.x <= mx <= self.x + self.width:
                if self.y <= my <= self.y + self.width:
                    if len(turns) % 2 == 0:
                        board[row][col] = 'o'
                    turns.append(1)
                    self.clicked = True
def computer_click(boxes, turn):
    if not len(turn) % 2 == 0:
        choice = 0
        current_box = 0
        bestScore = -9999
        bestMove = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                choice += 1
                if board[row][col] == '':
                    board[row][col] = 'x'
                    score = minimax(0, False, boxes)
                    board[row][col] = ''
                    if score > bestScore:
                        current_box = choice
                        bestMove = [row, col]
                        bestScore = score
        turn.append(1)
        board[bestMove[0]][bestMove[1]] = 'x'
        boxes[current_box - 1].clicked = True
        if check_winner(board):
            can_play = False



def check_winner(board):
    if ['x', 'x', 'x'] in board:
        return 'x'
    if ['o', 'o', 'o'] in board:
        return 'o'
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        return 'x'
    if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        return 'x'

    if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        return 'o'
    if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        return 'o'
    every_cell = 0
    for col in range(len(board)):
        xs = 0
        os = 0
        for row in range(len(board[0])):
            if board[row][col] == 'x':
                every_cell += 1
                xs += 1
            if xs == 3:
                return 'x'
            if board[row][col] == 'o':
                every_cell += 1
                os += 1
            if os == 3:
                return 'o'
    if every_cell == 9:
        return 'tie'


def minimax(depth, isMaximizing, boxes):
    # print(x, o)
    result = check_winner(board)
    if result:
        return scores[result]
    if isMaximizing:
        bestScore = -999
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '':
                    board[row][col] = 'x'
                    score = minimax(depth + 1, False, boxes)
                    board[row][col] = ''
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 999
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '':
                    board[row][col] = 'o'
                    score = minimax(depth + 1, True, boxes)
                    board[row][col] = ''
                    bestScore = min(score, bestScore)
        return bestScore


def draw_boxes(boxes):
    cols = 0
    row = 0
    x = 0
    y = 0
    for i, bx in enumerate(boxes):
        bx.draw(win, x, y)
        bx.index = [row, cols]
        bx.num = i + 1
        x += bx.width
        cols += 1
        if cols % 3 == 0 and cols != 0:
            y += bx.width
            row += 1
            x = 0
            cols = 0


def RedrawGameWindow(boxes):
    win.fill(0)
    draw_boxes(boxes)
    pygame.display.update()


def main():
    global can_play
    running = True
    boxes = [box() for _ in range(9)]
    turn = [1]
    while running:
        RedrawGameWindow(boxes)
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pos = pygame.mouse.get_pos()
        m = pygame.mouse.get_pressed()
        if not len(turn) % 2 == 0 and can_play:
            computer_click(boxes, turn)
        if m[0]:
            if can_play:
                for bx in boxes:
                    bx.click(pos, turn)
                if check_winner(board):
                    can_play = False

main()