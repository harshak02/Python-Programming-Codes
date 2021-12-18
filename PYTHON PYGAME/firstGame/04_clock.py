import pygame

pygame.init()

screen_height = 600
screen_width = 900

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Snake Xperia")
pygame.display.update()

exit_game = False
game_over = False

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

snake_x = 45
snake_y = 55
snake_size = 10

#______________________________fps__________________________________:-

fps = 30

#__________________________Creating Clock___________________________:-

clock = pygame.time.Clock()


while (not exit_game) :

    for event in pygame.event.get() :
        if (event.type==pygame.QUIT) :
            exit_game = True

        if (event.type==pygame.KEYDOWN) :
            if(event.key==pygame.K_RIGHT) :
                snake_x = snake_x + 10


    gameWindow.fill(white)

    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()

    #here after update we need to add clock
    clock.tick(fps)


pygame.quit()
quit()

 
