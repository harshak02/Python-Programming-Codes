import pygame
import random

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

velocity_x = 0
velocity_y = 0

#_____________________________increase Lenght_____________________:-

snk_list = []# we need to append with list of co-ordinates
snk_lenght = 1

#imp :-
init_velocity = 5 #default velocity

#for our ease coz we are in devolopment mode :-
food_x = random.randint(20,screen_width/2)
food_y = random.randint(20,screen_height/2)
food_size = 10

score = 0

fps = 30
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,50)

def text_score(text,color,x,y) :

    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])#list of co-ordinates


def plot_snake(gameWindow,color,snk_list,snake_size) :

    for snake_x,snake_y in snk_list :
        pygame.draw.rect(gameWindow,color,[snake_x,snake_y,snake_size,snake_size])


while (not exit_game) :

    for event in pygame.event.get() :

        #these are button pressed one time changes

        if (event.type==pygame.QUIT) :
            exit_game = True

        if (event.type==pygame.KEYDOWN) :
            if(event.key==pygame.K_RIGHT) :
                velocity_x = init_velocity
                velocity_y = 0

        if (event.type==pygame.KEYDOWN) :
            if(event.key==pygame.K_LEFT) :
                velocity_x = -init_velocity
                velocity_y = 0

        if (event.type==pygame.KEYDOWN) :
            if(event.key==pygame.K_UP) :
                velocity_y = -init_velocity
                velocity_x = 0

        if (event.type==pygame.KEYDOWN) :
            if(event.key==pygame.K_DOWN) :
                velocity_y = init_velocity
                velocity_x = 0

    #these are time running variables and changes
    #real time variables

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if (abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6) :

        score = score+1
        #compulsorily this should be string

        food_x = random.randint(20,screen_width/2)
        food_y = random.randint(20,screen_height/2)
        
        snk_lenght+=5


    gameWindow.fill(white)
    #displayScore should come here :-
    text = "Score :" +" "+str(score*10)
    text_score(text,red,5,5)

    #imp
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    #append all new new head positions

    #imp
    if(len(snk_list)>snk_lenght) :
        del snk_list[0]

    # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(gameWindow,black,snk_list,snake_size)
    pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
    pygame.display.update()

    clock.tick(fps)


pygame.quit()
quit()






