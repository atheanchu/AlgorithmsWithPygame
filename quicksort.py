import pygame, sys, random

# Let's draw 400X400 board
height = 400
width = 400
rectWidth = 10
rects = []

class Rect :

    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.x = x
        self.y = y 
        self.w = w
        self.h = h

    def show(self, color) : 
        global screen 
        pygame.draw.rect(screen, color, (self.x, self.y, self.w, -self.h), 3)

    def get(self):
        return self.h

def quicksort(arr, start, end): 
    if start >= end:
        return 
    index = partition(arr, start, end)
    quicksort(arr, start, index-1)
    quicksort(arr, index + 1, end)

def partition(arr, start, end):
    pivotValue = arr[end].get()
    pivotIndex = start 

    for i in range(start, end):
        if arr[i].get() < pivotValue : 
            swap(arr, i, pivotIndex)
            pivotIndex += 1 
    
    swap(arr, pivotIndex, end)

    return pivotIndex

def swap(arr, i, j) : 
    arr[i].show((255,0,0))
    arr[j].show((0,255,0))
    arr[i].show((51,51,51))
    arr[j].show((51,51,51))
    arr[i].h, arr[j].h = arr[j].h, arr[i].h
    pygame.time.delay(100)
    arr[i].show((255,0,0))
    arr[j].show((0,255,0))
    pygame.display.update()

pygame.init()

screen = pygame.display.set_mode((width, height))


for i in range(int(width / rectWidth)):
    rectHeight = random.randint(0, height)
    rects.append(Rect(screen, i * rectWidth, height, rectWidth, rectHeight))

screen.fill(pygame.Color(51, 51, 51))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            quicksort(rects, 0, len(rects) - 1)
    
    for rect in rects:
        rect.show((255,255,255))

    pygame.display.update()
