
import pygame              
import random     
from insert import insert_player_result
from update import update_person
from get_player import get_player_data

pygame.init() 

SW, SH = 600, 600 # screen size(playing area)
WW, WH = 600, 700 # window size
WIDTH, HEIGHT = 800, 600


BLOCK_SIZE = 40
FONT = pygame.font.SysFont("Futura", BLOCK_SIZE)    
font = pygame.font.Font(None, 36)


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("snake")
clock = pygame.time.Clock() # to controlling the game's speed

def get_player_name():
    name = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        screen.fill(BLACK)
        draw_text("Введите ваше имя:", font, WHITE, (WW // 2, WH // 2 - 50))
        draw_text(name, font, WHITE, (WW // 2, WH // 2))
        pygame.display.flip()
        clock.tick(10)
    return name

# Отрисовка текста
def draw_text(text, font, color, pos):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = pos
    screen.blit(text_surface, text_rect)


class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) # rectangle for the snake's head
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)] # snake's body as a list of rectangles
        self.dead = False # flag indicating whether the snake is dead
        self.restart = False # flag indicating whether the restart key has been pressed

    def update(self):
        global apple, wall, golden_apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y: # checking for collision of the snake's head with its body
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH): # checking if the snake leaves the playing area
                self.dead = True
        # restarting the game if the snake is dead and the restart is true
        if self.dead and self.restart:
                self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
                self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
                self.xdir = 1
                self.ydir = 0
                self.dead = False
                self.restart = False
                apple = Apple() # creating a new apple
                wall = Wall() # creating a new wall
                golden_apple = GoldenApple(self.body, (apple.x, apple.y), [barrier for barrier in wall.barriers]) # creating a new golden apple
        # updating the snake's position
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.spawn_apple()
        self.spawn_time = pygame.time.get_ticks() 
    # method for generating a new position for the apple
    def spawn_apple(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
    # method for updating the position and drawing the apple
    def update(self, snake_body): 
        if pygame.time.get_ticks() - self.spawn_time >= 5000: # 5000 => milliseconds 
            self.spawn_apple() 
            self.spawn_time = pygame.time.get_ticks()
        while (self.x, self.y) in [(square.x, square.y) for square in snake_body]:
            self.spawn_apple()
        self.new_apple = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, "red", self.new_apple)

class GoldenApple:
    def __init__(self, snake_body, apple_pos, wall_barriers):
        # initializing the golden apple's spawn time and its rectangle
        self.spawn_time = pygame.time.get_ticks()
        self.golden_apple_rect = None
        if random.random() <= 0.1: # call spawn_golden_apple if a random number is less than or equal to 0.1 (probability 10%)
            self.spawn_golden_apple(snake_body, apple_pos, wall_barriers) 
    # method for spawning a golden apple
    def spawn_golden_apple(self, snake_body, apple_pos, wall_barriers):
        while True:
            self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            # checking if the generated coordinates do not overlap with the snake's body, regular apple, or wall barriers
            if (self.x, self.y) not in apple_pos and \
               (self.x, self.y) not in [(square.x, square.y) for square in snake_body] and \
               (self.x, self.y) not in [(barrier.x, barrier.y) for barrier in wall_barriers]:
                # creating a rectangle representing the golden apple
                self.golden_apple_rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                break
    # method for updating the golden apple's position and appearance
    def update(self, snake_body, apple_pos, wall_barriers):
        current_time = pygame.time.get_ticks()

        if self.golden_apple_rect is not None: # checking if a golden apple exists 
            if current_time - self.spawn_time >= 3000: # if it exists, checking if it's time to despawn it (3 seconds)
                self.golden_apple_rect = None  
        else: # if does not exist, checks whether a new one needs to be created
            if random.random() <= 0.1:  
                self.spawn_golden_apple(snake_body, apple_pos, wall_barriers)
                self.spawn_time = current_time

        if self.golden_apple_rect is not None: # drawing the golden apple if it exists
            pygame.draw.rect(screen, "gold", self.golden_apple_rect)

class Wall:
    def __init__(self):
        self.barriers = []
    # method for generating new barriers (walls)
    def spawn_barrier(self, snake_body, apple_pos, snake_head_pos):
        while True:
            self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            new_barrier = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) 
            # condition ensures that the newly generated barrier does not collide with any part of the snake's body and does not overlap with the position of the apple 
            if new_barrier.collidelist(snake_body) == -1 and new_barrier.collidepoint(apple_pos) == False:
                # condition ensures that the new barrier is not placed too close to the snake's head. (barrier is at least three blocks away from the snake's head)  
                if abs(snake_head_pos[0] - new_barrier.x) > 3 * BLOCK_SIZE or abs(snake_head_pos[1] - new_barrier.y) > 3 * BLOCK_SIZE:
                    self.barriers.append(new_barrier)
                    break    
    # method for updating and drawing the walls
    def update(self, snake_body, apple_pos, snake_head_pos, eaten_fruits):
        for barrier in self.barriers:
            pygame.draw.rect(screen, "blue", barrier)
            if barrier.colliderect(snake_head_pos): # checking for collision with added barriers
                snake.dead = True

        eaten_fruits = eaten_fruits // 2 # this means that a new barrier is added after every second fruit eaten.
        if eaten_fruits > len(self.barriers):
            for _ in range(eaten_fruits - len(self.barriers)):
                self.spawn_barrier(snake_body, apple_pos, snake_head_pos)
# function for drawing the game grid
def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (60, 60, 60), rect, 1)


player = get_player_name()
# initializing score, speed, and eaten fruits variables
crocodile = get_player_data(player)
if get_player_data(player) == None:
    score = speed = eaten_fruits = 0
else:
    score = crocodile[3]
    speed = crocodile[4]
    eaten_fruits = crocodile[2]*2

'''score = speed = eaten_fruits = 0'''
scoretxt = speedtxt = leveltxt = FONT.render("0", True, "white")
score_rect = scoretxt.get_rect(center=(20, 620))
speed_rect = speedtxt.get_rect(center=(20, 660))
level_rect = leveltxt.get_rect(center=(480, 620))

drawGrid()
# creating a objects of game 
snake = Snake()
apple = Apple()
wall = Wall()
golden_apple = GoldenApple(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])
borrowed_length=score//5+1
done=False
paused=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # exit the game
                done = True
            elif event.key == pygame.K_SPACE: # restart the game
                snake.restart = True
                score = speed = eaten_fruits = 0
            elif event.key == pygame.K_p:
                paused = not paused
            if not paused:
                if event.key == pygame.K_DOWN: 
                    snake.ydir = 1
                    snake.xdir = 0
                elif event.key == pygame.K_UP:
                    snake.ydir = -1
                    snake.xdir = 0
                elif event.key == pygame.K_RIGHT:
                    snake.ydir = 0
                    snake.xdir = 1
                elif event.key == pygame.K_LEFT:
                    snake.ydir = 0
                    snake.xdir = -1
    if not paused:
        snake.update()

        screen.fill("black")

        drawGrid()

        wall.update(snake.body, (apple.x, apple.y), snake.head, eaten_fruits)

        apple.update(snake.body)

        golden_apple.update(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])
    

    pygame.draw.rect(screen, (0, 255, 0), snake.head) # drawing the snake's head
    pygame.draw.rect(screen, (42, 42, 42), [0, SH, WW, WH]) # drawing the surface for showing some statistics
    # drawing the current values of score, speed, and level 
    scoretxt = FONT.render(f"score: {score}", True, (138, 154, 91)) 
    speedtxt = FONT.render(f"speed: {speed + 5}", True, (96, 130, 182))
    leveltxt = FONT.render(f"level: {eaten_fruits//2}", True, (207, 159, 255))
    # displaying the score, speed, and level on the screen
    screen.blit(scoretxt, score_rect)
    screen.blit(speedtxt, speed_rect)
    screen.blit(leveltxt, level_rect)

    # drawing the snake's body
    for square in snake.body:
        pygame.draw.rect(screen, (0, 65, 0), square)

    # checking if a golden apple exist in screen and x,y of head == x,y of apple
    if golden_apple.golden_apple_rect is not None and snake.head.colliderect(golden_apple.golden_apple_rect): # working like red apple, but score->3
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        golden_apple = GoldenApple(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])
        eaten_fruits += 1
        score += 3
        if (len(snake.body)-1) % 5 == 0: 
            speed += 0.5

    if len(snake.body)<borrowed_length:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
    # checking if a x,y of head == x,y of apple
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE)) 
        apple = Apple() # creating a new apple, after snake has eaten current apple 
        eaten_fruits += 1
        score += 1
        if (len(snake.body)-1) % 5 == 0: # this means that speed is increasing after every fifth fruit eaten.
            speed += 0.5

    # checking that a new apple will not be created on an existing barrier
    for barrier in wall.barriers:
        if apple.x == barrier[0] and apple.y == barrier[1]: # else regenerate new position for apple
            apple.spawn_apple()

    # game over when the snake dies
    if snake.dead and not snake.restart:
        screen.fill("black")
        endtxt = FONT.render(f"your score: {score}", True, "red") 
        end_rect = endtxt.get_rect(center=(SW/2, SH/2))
        screen.blit(endtxt, end_rect)
        done = not done
        if get_player_data(player) == None:
            insert_player_result(name=player, level=(eaten_fruits // 2), score=score, speed=speed)
        else:
            update_person(name=player, level=(eaten_fruits // 2), score=score, speed=speed)
    if paused:
        draw_text("PAUSED", FONT, WHITE, (SW // 2, SH // 2))


    pygame.display.update() # updating the screen
    clock.tick(5 + speed) # using fps to control game speed

pygame.quit()