import pygame 
import time
import random

pygame.init() # ??

# color of each sanke block
black = (0, 0, 0)

# font for game over msg
red = (255, 0, 0)


white = (255, 255, 255)

# background color
blue = (0, 0, 255)

# font color for score
yellow = (255, 255, 102) 

# color of food
green = (0, 255, 0)


# dimensions of display
dis_width = 600
dis_height = 400

# dis variable can be used later to render 
# graphical element on display
dis=pygame.display.set_mode((dis_width,dis_height)) 


#updates changes made to the screen
pygame.display.update() 

# adds caption at the top of game window
pygame.display.set_caption('Snake game by Rohit')

# for slowing loop
clock = pygame.time.Clock() 

# height and width of each block of snake
# also height and width of food 
snake_block = 10 
# speed of loop
snake_speed = 15 

# using built in function for font for showing game over
font_style = pygame.font.SysFont("bahnschrift", 25) 
# font for score
score_font = pygame.font.SysFont("comicsansms", 35) 


# function for updating score
def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0,0])


# draws snake 
def our_snake(snake_block, snake_List):
    # snake_List is list of co-ordinates of each block of snake
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# adds msg on display
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# function for starting game
def gameLoop():
    # closes game window when value is true
    game_over = False
    # turns true after hitting wall or itself
    game_close = False
    # turns true after pressing spacebar 
    game_pause = False

    # initial co-ordinate of head of snake
    x1 = dis_width/2
    y1 = dis_height/2    

    # change in co-ordinate of head of snake in each iteration
    x1_change = 0
    y1_change = 0

    # list of each block of snake
    snake_List = []
    # initial length of snake
    Length_of_snake = 1

    # initial co-ordinate of food
    # co-ordinate of snake is always multiple of 10
    # therefore divide and multiply by 10
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10

    # this loop runs the game 
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
                        # recursion
                        gameLoop()


        # loop for listening event
        # events: window close, arrow keys
        for event in pygame.event.get():

            # close window
            if event.type == pygame.QUIT: 
                game_over = true

            # key press to navigate snake
            # x1_change value can be altered 
            # even when game is paused
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
                elif event.key == pygame.K_SPACE:
                        game_pause = not(game_pause)

        # condition for hitting wall
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True


        if not(game_pause):
            x1 += x1_change
            y1 += y1_change

            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0] # delete past posn of tail

            # checks whether snake bite itself
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True



        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

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

# starts game
gameLoop()