import pygame

x = pygame.init()
print(x)

gameWindow = pygame.display.set_mode((1200,500))

pygame.display.set_caption("My first Game")

exit_game = False
game_over = False
#colours and bonus all are variables

#_______________________Event Handling___________________:-

while (not exit_game) :
    for event in pygame.event.get() :
        print(event)
        #gives all responses

pygame.quit()
quit()


