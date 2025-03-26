import pygame
from datetime import datetime, timedelta

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

surface = pygame.Surface((100, 100))
clock_picture= pygame.image.load('lab7/clock.png')
default_image_size=(280,210)
default_image_size2=(280,210)
default_image_size3=(12,210)
clock_picture=pygame.transform.scale(clock_picture,default_image_size)
minute = pygame.image.load('lab7/rightarm.png')
minute=pygame.transform.scale(minute,default_image_size2)
second = pygame.image.load('lab7/leftarm.png')
second=pygame.transform.scale(second,default_image_size3)



pygame.init()

screen = pygame.display.set_mode((280, 210))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        today = datetime.now().time()
        minute_number=today.minute
        seconds_number=today.second
        screen.fill((0, 0, 0))
        screen.blit(clock_picture, (0, 0))
        list=rot_center(minute,-6*minute_number-45,140,105)
        screen.blit(list[0],list[1])
        list=rot_center(second,-6*seconds_number,140,105)
        screen.blit(list[0],list[1])
        pygame.display.flip()
        clock.tick(60)
        print(today)