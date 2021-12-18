import pygame 

pygame.init()

screen_height = 600
screen_width = 900

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Snake Xperia")
pygame.display.update()

exit_game = False
game_over = False

#__________________________colours__________________________:-

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

while (not exit_game) :

    for event in pygame.event.get() :
        if (event.type==pygame.QUIT) :
            exit_game = True


    gameWindow.fill(white)
    pygame.display.update()
    #this update is used for updating anything in display


pygame.quit()
quit()


