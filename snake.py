import pygame
import numpy as np

pygame.init()

screen_width = 800
screen_height = 600
dis = pygame.display.set_mode((screen_width,screen_height)) # initialize game window
pygame.display.set_caption('Snake by bgatesson') 

green = (0,255,0) # define colors
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

snake_body = 25 # snake object properties
snake_speed = 10

clock = pygame.time.Clock() 

font_style = pygame.font.SysFont("comicsansms", 20)
font_score = pygame.font.SysFont("comicsansms", 20)

def message(msg,color,range): # message function
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, range)

def player_score(score): # score display function
    val = font_score.render("Score: " + str(score), True, white)
    dis.blit(val, [0,0])

def snake(snake_body, snake_list): # snake object function
    for n in snake_list:
        pygame.draw.rect(dis,green,[n[0],n[1],snake_body,snake_body])

def GameLoop():
    game_over = False
    game_menu = False

    x = screen_width / 2 # initial player position
    y = screen_height / 2

    x_new = 0
    y_new = 0

    snakeList = []
    snakeLength = 1

    food_x = np.random.randint(0,screen_width/25)*25 # generate random food coordinates
    food_y = np.random.randint(0,screen_height/25)*25

    while not game_over:

        while game_menu == True: # losing menu 
            dis.fill(black)
            message("Get good loser", white, [310,250])
            message("Press Q to quit or R to retry", white, [250,285])
            player_score(snakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get(): # options for player to retry or quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_menu = False
                    if event.key == pygame.K_r:
                        GameLoop()

        for event in pygame.event.get(): # snake directions controls
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_new = snake_body
                    y_new = 0
                elif event.key == pygame.K_LEFT:
                    x_new = -snake_body
                    y_new = 0
                elif event.key == pygame.K_UP:
                    y_new = -snake_body
                    x_new = 0
                elif event.key == pygame.K_DOWN:
                    y_new = snake_body
                    x_new = 0
    
        if x >= screen_width or x < 0 or y >= screen_height or y < 0: # lose when running into the border
            game_menu = True

        x += x_new
        y += y_new

        dis.fill(black)
        pygame.draw.rect(dis,red,[food_x,food_y,snake_body,snake_body]) # create snake object
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for n in snakeList[:-1]: # lose when snake comes into contact with its own body
            if n == snakeHead:
                game_menu = True
        
        snake(snake_body, snakeList)
        player_score(snakeLength - 1)

        pygame.display.update()

        if x == food_x and y == food_y: # when touching food block, gain length
            food_x = np.random.randint(0,screen_width/25)*25
            food_y = np.random.randint(0,screen_height/25)*25
            snakeLength += 1

        clock.tick(snake_speed) # set snake speed

    pygame.quit()
    quit()

GameLoop()
