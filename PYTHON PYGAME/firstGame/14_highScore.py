import pygame
import random

pygame.init()

screen_height = 600
screen_width = 900

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Snake Xperia")
pygame.display.update()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

font = pygame.font.SysFont(None,50)

def text_score(text,color,x,y) :

    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])#list of co-ordinates


def plot_snake(gameWindow,color,snk_list,snake_size) :

    for snake_x,snake_y in snk_list :
        pygame.draw.rect(gameWindow,color,[snake_x,snake_y,snake_size,snake_size])

#_________________________creating Game loop function____________________:-
#it should inclue all game varibales and the values that are chnaging acc to time

def gameLoop() :

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10

    #imp
    f = open("highScore.txt","r")
    high_score = f.read()
    f.close()

    velocity_x = 0
    velocity_y = 0

    snk_list = []# we need to append with list of co-ordinates
    snk_lenght = 1
    init_velocity = 5 

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    food_size = 10

    score = 0

    fps = 30
    clock = pygame.time.Clock()

    while (not exit_game) :


        if (game_over) :

            f = open("highScore.txt","w")
            f.write(str(high_score))
            f.close()

            gameWindow.fill(black)
            text_final = "Game Over!!!"
            text_return = "Enter 'Return' Button To Play Again"
            score_final = score
            text_score(text_final,blue,300,250)
            text_score("Your Score is : "+str(score_final),green,280,200)
            text_score(text_return,red,175,300)


            for event in pygame.event.get() :

                if (event.type==pygame.QUIT) :
                    exit_game = True

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_RETURN) :
                        gameLoop()

        else :
            
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

                score+=10
                #compulsorily this should be string

                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                
                snk_lenght+=5

                if(score>int(high_score)) :
                    high_score = score

            
            gameWindow.fill(white)

            #displayScore should come here :-
            text = "Score :" + " "+str(score) + "  High Score :" + " " + str(high_score)
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

            if(head in snk_list[:-1]) :#excludes -1 coz -1 is head
                game_over = True


            #setting screen width collision
            if((snake_x<0) or (snake_x>screen_width) or (snake_y<0) or (snake_y>screen_height)) :
                game_over = True

            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)

            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
        pygame.display.update()

        clock.tick(fps)



    pygame.quit()
    quit()

gameLoop()
