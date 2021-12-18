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

#imp :-
init_velocity = 5 #default velocity

#for our ease coz we are in devolopment mode :-
food_x = random.randint(20,screen_width/2)
food_y = random.randint(20,screen_height/2)
food_size = 10

#_____________________________score_____________________________:-

score = 0

fps = 30
clock = pygame.time.Clock()

#______________________addingScoreToDisplay_______________________:-

font = pygame.font.SysFont(None,50)
# font = pygame.font.sysFont(systemFont,font size)

def text_score(text,color,x,y) :
    #text -> what text shall we put
    #colour -> what colour 
    #x -> x coordinate
    #y -> y coordinate
    screen_text = font.render(text,True,color)
    #for updating :-
    gameWindow.blit(screen_text,[x,y])#list of co-ordinates


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


    gameWindow.fill(white)
    #displayScore should come here :-
    text = "Score :" +" "+str(score*10)
    text_score(text,red,5,5)

    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
    pygame.display.update()

    clock.tick(fps)


pygame.quit()
quit()




