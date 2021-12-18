import pygame

#________________activating pygame______________:-

x = pygame.init()

#________________Checking installed modules_____:-

print(x)
#this will give a tuple with (x,y) x->activated module 
#y-> gives unistalled modules... default is (7,0)

#________________ Display of game________________:-

gameWindow = pygame.display.set_mode((1200,500))

#________________ Setting name of game________________:-

pygame.display.set_caption("My first Game")

#________________ Setting variables of Game____________:-

exit_game = False
game_over = False


