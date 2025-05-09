import pygame

''' Get Figure '''

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    return (x, y, w, h)
    
def getCircle(x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    radius = max(abs(x1 - x2), abs(y1 - y2)) // 2
    return (x, y, radius)
   
def getSquare(x1, y1, x2, y2):
    side = max(abs(x1 - x2), abs(y1 - y2))
    x = x1 if x1 < x2 else x1 - side
    y = y1 if y1 < y2 else y1 - side
    return (x, y, side, side)

def getRightTriangle (x1, y1, x2, y2):
    return ((x1,y1),(x1,y2),(x2,y2))
    
def getEquilateraltriangle (x1, y1, x2, y2):
    n=(x1+x2)/2
    h=abs(x1-x2)*0.866025
    if y1-y2>0:
        return ((x1,y1),(x2,y1),(n,y1-h))
    else:
        return ((x1,y1),(x2,y1),(n,y1+h))

def getRhombus (x1, y1, x2, y2):
    n=(x1+x2)/2
    m=(y1+y2)/2
    return ((n,y1),(x2,m),(n,y2),(x1,m))

def color_selection(current_color):
    if blackButton.collidepoint(event.pos):
        current_color = BLACK
    elif redButton.collidepoint(event.pos):
        current_color = RED
    elif yellowButton.collidepoint(event.pos):
        current_color = YELLOW
    elif blueButton.collidepoint(event.pos):
        current_color = BLUE
    elif brownButton.collidepoint(event.pos):
        current_color = BROWN 
    elif purpleButton.collidepoint(event.pos):
        current_color = PURPLE
    elif pinkButton.collidepoint(event.pos):
        current_color = PINK
    elif greenButton.collidepoint(event.pos):
        current_color = GREEN  
    return current_color


def figure_selection(figure_index):
    if rectButton.collidepoint(event.pos):
        figure_index = 0
    elif circleButton.collidepoint(event.pos):
        figure_index = 1
    elif squareButton.collidepoint(event.pos):
        figure_index = 2
    elif rightTriangleButton.collidepoint(event.pos):
        figure_index = 3
    elif equilateraltriangleButton.collidepoint(event.pos):
        figure_index = 4
    elif rhombusButton.collidepoint(event.pos):
        figure_index = 5
    return figure_index

def thickness_selection(th_index):
    font = pygame.font.SysFont("comicsansms", 55)    
    text = font.render(str(sizes[th_index]), True, BLACK)
    screen.blit(text, (170, 20))

def isClear():
    if clearButton.collidepoint(event.pos):
        screen.fill(WHITE)
        another_layer.fill(WHITE)

# Set Constants(color, window size, frames per second)
BLACK = (0, 0, 0)      
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BROWN = (156, 42, 42)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255) # for eraser
WIDTH, HEIGHT = 800, 700 
FPS = 60
background_color = 	(0,0,205)
sizes = [1, 3, 5, 7, 9] # list with sizes of thickness

figures = [0, 1] # 0 -> rect  1 -> circle

# changable parameters
th_index = 2 # current size of thickness
current_thickness = sizes[th_index]

current_color = BLACK

figure_index = 0
current_figure = figures[figure_index]

pygame.init()  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
another_layer = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10


clear0 = pygame.image.load('clear2.png')
clearImage = pygame.transform.scale(clear0, (40, 40))

# main logic
done = False
isMouseDown = False
# fill blackground
screen.fill(WHITE)
another_layer.fill(WHITE)


''' Main Loop'''

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        
        ''' Thickness Selection With Keyboard '''

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True 
            if event.key == pygame.K_UP:
                th_index += 1
                if th_index == len(sizes):
                    th_index = 0 
            if event.key == pygame.K_DOWN:
                th_index -= 1
                if th_index == -1:
                    th_index = len(sizes) - 1
             
        ''' Draw Shape(rect & circle) With Mouse '''
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click: 
                x1 = event.pos[0]
                y1 = event.pos[1]
                isMouseDown = True        
                isClear() # clear check
        
                figure_index = figure_selection(figure_index)
                current_color = color_selection(current_color)
    
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # left click
                isMouseDown = False
                another_layer.blit(screen, (0, 0))   
                 
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                x2 = event.pos[0]
                y2 = event.pos[1]
                screen.blit(another_layer, (0, 0))
                if figure_index == 0:
                    pygame.draw.rect(screen, current_color, getRectangle(x1, y1, x2, y2), current_thickness)
                elif figure_index== 1:
                    pygame.draw.circle(screen, current_color, getCircle(x1, y1, x2, y2)[:2], getCircle(x1, y1, x2, y2)[2], current_thickness)
                elif figure_index == 2:
                    pygame.draw.rect(screen, current_color, getSquare(x1, y1, x2, y2), current_thickness)
                elif figure_index == 3:
                    pygame.draw.polygon(screen, current_color, getRightTriangle(x1, y1, x2, y2), current_thickness)
                elif figure_index == 4:
                    pygame.draw.polygon(screen, current_color, getEquilateraltriangle (x1, y1, x2, y2), current_thickness)
                elif figure_index == 5:
                    pygame.draw.polygon(screen, current_color, getRhombus (x1, y1, x2, y2), current_thickness)
        
                

                
    ''' Main Menu '''  
    #фоны кнопок
    menuSurface = pygame.draw.rect(screen, (100,149,237), [0, 0, WIDTH, 105])
    shapeSurface = pygame.draw.rect(screen, background_color, [5, 5, 140, 95])
    thicknessSurface = pygame.draw.rect(screen, background_color, [160, 35, 50, 50])
    colorSurface = pygame.draw.rect(screen, 'white', [616, 5, 179, 92])

    clearButton = screen.blit(clearImage, (530, 5))  

    rectButton = pygame.draw.rect(screen, 'black', (10, 15, 40, 30), 3) 
    circleButton = pygame.draw.circle(screen, 'black', (70, 30), 15, 3)
    squareButton = pygame.draw.rect(screen, 'black', (10,50,40,40),3)
    rightTriangleButton = pygame.draw.polygon(screen, 'black', ((55,50),(55,89),(85,89)), 3)
    equilateraltriangleButton = pygame.draw.polygon(screen, 'black', ((120,85),(105,55),(90,85)), 3)
    rhombusButton = pygame.draw.polygon(screen, 'black', ((90,30),(105,45),(120,30),(105,15)), 3)

    blackButton = pygame.draw.rect(screen, 'black', (620, 9, 40, 40))  
    redButton = pygame.draw.rect(screen, 'red', (664, 9, 40, 40))      
    yellowButton = pygame.draw.rect(screen, 'yellow', (708, 9, 40, 40))
    blueButton = pygame.draw.rect(screen, 'blue', (752, 9, 40, 40))
    brownButton = pygame.draw.rect(screen, 'brown', (620, 53, 40, 40))
    purpleButton = pygame.draw.rect(screen, 'purple', (664, 53, 40, 40))
    pinkButton = pygame.draw.rect(screen, 'pink', (708, 53, 40, 40))
    greenButton = pygame.draw.rect(screen, 'green', (752, 53, 40, 40))

    # Changes in menu
    current_thickness = sizes[th_index]
    thickness_selection(th_index)
    
    pygame.display.flip()
    clock.tick(FPS)