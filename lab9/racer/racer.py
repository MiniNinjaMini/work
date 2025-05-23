# библиотеки
import random
import time

import pygame
import sys
from pygame.locals import *

pygame.init()

# фпс
FPS = 60
FramePerSec = pygame.time.Clock()

# цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
COIN_COUNTER = 0
# шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# фон
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #проверяем зажатую кнопку и двигаем машинку

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def collect_coin(self, coins):
        global SCORE
        for coin in coins:
            if abs(self.rect[0]-coin.rect[0])<44 and abs(self.rect[1]-coin.rect[1])<42:  # Check if player collides with coin
                '''print('yappy')'''
                SCORE+= coin.points
                coins.remove(coin)
                all_sprites.remove(coin)  # Remove coin from the group
                return True
                
            '''print('chtoto')
            print(coin.rect)
            print(coin.rect[0])
            print(self.rect)
            print(abs(self.rect[0]-coin.rect[0]))
            print(abs(self.rect[1]-coin.rect[1]))'''
        return False # No coin collected

    

coin=pygame.image.load("coin1.png")
red_coin_image = pygame.image.load("red_coin.png")
orange_coin_image=pygame.image.load("orange_coin.png")

class Coin(pygame.sprite.Sprite):
    def __init__(self, image, points):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.points = points

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
class RedCoin(Coin):
    def __init__(self):
        super().__init__(red_coin_image, 5)

class OrangeCoin(Coin):
    def __init__(self):
        super().__init__(orange_coin_image, 3)
# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin(coin,1)

# создаем множества содержащие наши спрайты
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# добавляем ивент ускрорения
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 5000)

done = False

#  сама игра
while not done:

    # проверка ивентов
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # выход
                done = True

    DISPLAYSURF.blit(background, (0, 0))

    #скор и коины
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    legend = pygame.image.load("costs.png")

    DISPLAYSURF.blit(legend, (10, 20))
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (300, 10))

    # отрисовка спрайтов на экране и обновление их положения
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # увеличиваем скор и создаем новый коин при сборе
    if P1.collect_coin(coins):
        pygame.mixer.Sound("GetCoin.mp3").play()
        COIN_SCORE += 1
        number=random.random()
        if number < 0.6:
            new_coin = Coin(coin, 1)
        elif number <0.9:
            new_coin = OrangeCoin()
        else:
            new_coin = RedCoin() 
        coins.add(new_coin)
        all_sprites.add(new_coin)
        if COIN_SCORE%4==0:
            pygame.event.post(pygame.event.Event(INC_SPEED))
        #print(SPEED)

    # случай аварии
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
