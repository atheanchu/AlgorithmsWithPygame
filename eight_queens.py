import pygame, sys

# Global Variables
width = 800
height = 800
SIZE = 100
board = []
result = 0
done = False
put = []

# Color preset
rect_border_color = (255,255,255)
bg_color = (51,51,51)
placed_color = (0,255,0)

# Rect Class
class Rect :

    def __init__(self, x, y) :
        self.x = x 
        self.y = y
        self.placed = False
    
    def show(self, color = rect_border_color):
        global screen, SIZE 
        pygame.draw.rect(screen, color, (self.x, self.y, SIZE, SIZE), 3)

    def place(self):
        self.placed = True 
        pygame.draw.rect(screen, placed_color, (self.x, self.y, SIZE, SIZE))
    
    def unplace(self): 
        self.placed = False
        pygame.draw.rect(screen, bg_color, (self.x, self.y, SIZE, SIZE))
        pygame.draw.rect(screen, rect_border_color, (self.x, self.y, SIZE, SIZE), 3)

def backtrack(board, row) : 
    global result
    
    # find the available position in the current row
    for col in range(len(board[row])):
        if couldplace(board, row, col): 
            placeQueen(board, row, col)
            if row == len(board) - 1 :
                result += 1
                print("Found so far..." , result)
                pygame.time.delay(5000)
            else :
                backtrack(board, row+1)
            removeQueen(board, row, col)

def placeQueen(board, r, c) : 
    board[r][c].place()
    put.append([r, c])
    pygame.display.update()

def removeQueen(board, r, c) : 
    board[r][c].unplace()
    put.remove([r, c])
    pygame.display.update()

def couldplace(board, row, col) :
    for pos in put: 
        # Check column
        if col == pos[1]: 
            return False 
        if abs(pos[0] - row) == abs(pos[1] - col):
            return False
    return True 

# Create 8X8 board
for i in range(int(width/SIZE)) :
    new = []
    for j in range(int(height/SIZE)) :
        new.append(Rect(j * SIZE, i * SIZE))
    board.append(new)

screen = pygame.display.set_mode((width, height))
screen.fill(pygame.Color(bg_color))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            backtrack(board, 0)
            print(result)
            pygame.quit()
            sys.exit()

    for i in range(len(board)) :
        for j in range(len(board[0])) :
            board[i][j].show()

    pygame.display.update()