import pygame

x = pygame.init()
print(x)

gameWindow = pygame.display.set_mode((1200,500))

pygame.display.set_caption("My first Game")

exit_game = False
game_over = False
#colours and bonus all are variables

while (not exit_game) :
    for event in pygame.event.get() :
        #______________Handling Quit Event____________:-
        if (event.type==pygame.QUIT) :
            exit_game = True

        #______________Handling KeyBoard Buttons_______:-
        if (event.type==pygame.KEYDOWN) :
            if(event.type==pygame.K_RIGHT) :
                print("Right key is pressed by user")

pygame.quit()
quit()
