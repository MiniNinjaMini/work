import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width,height))

head_square = [100,100]

done = False

#start of gameplay loop
while not done:
    #gameplay even conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if not head_square[1] + 20>575:
                    head_square[1] += 20
                else:
                    head_square[1] =575
            if event.key == pygame.K_UP:
                if not head_square[1] -20<25:
                    head_square[1] -= 20
                else:
                    head_square[1] =25
            if event.key == pygame.K_LEFT:
                if not head_square[0] -20<25:
                    head_square[0] -= 20
                else:
                    head_square[0]=25
            if event.key == pygame.K_RIGHT:
                if not head_square[0] +20>775:
                    head_square[0] += 20
                else:
                    head_square[0]=775
    
        
    #drawing section
    screen.fill((0,0,0))

    pygame.draw.circle(screen,(255,255,255),(head_square[0],head_square[1]),25)


    

    pygame.display.flip()
    pygame.time.delay(200)

pygame.quit()