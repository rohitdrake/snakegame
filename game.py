import pygame 
import time
import random

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)

dis_width = 600
dis_height = 400

# dis variable can be used later to render 
# graphical element on display
dis=pygame.display.set_mode((dis_width,dis_height)) 

pygame.display.update() #updates changes made to the screen
# adds caption at the top of game window
pygame.display.set_caption('Snake game by Rohit')












clock = pygame.time.Clock() # for slowing loop

snake_block = 10 # height and width of each block of snake
snake_speed = 15 # speed of loop

font_style = pygame.font.SysFont("bahnschrift", 25) # using built in function for font for showing game over
score_font = pygame.font.SysFont("comicsansms", 35) # font for score

def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0,0])


# draws snake 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# adds msg on display
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])



def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2    

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10


    while not game_over:

        # snake hits wall
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # loop for either playing again or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # loop for listening event
        # events: window close, arrow keys
        for event in pygame.event.get():

            # close window
            if event.type == pygame.QUIT: 
                game_over = true

            # key press to navigate snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:   
                        x1_change = snake_block
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0


        # condition for game over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
       # pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0] # delete past posn of tail

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # draws snake
        our_snake(snake_block, snake_List)
        # draws score
        Your_score(Length_of_snake - 1)

        # updates display after change.
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed) # slows down the speed of loop.



    pygame.quit()
    quit()

gameLoop()