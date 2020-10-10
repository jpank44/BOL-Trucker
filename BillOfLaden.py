# 10/2/2020
# snake with pygame from copy assignment
# My Idea to add my flavor to snake is to make it a game called 'BOL'
# 'BOL' is snake but allows you to return to a start point to deposit
# your snake load and earn points

import pygame
import random
# initializing pygame
pygame.init()

# colors
white = (255, 255, 255) # rgb format
red = (255, 0, 0)
black = (0, 0, 0)
orange = (255, 165, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("BOL")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
#[x, y, snake_size, snake_size] <--this provides pygame.draw.rect the coordinates and dimensions for snake

#homebase allows storage & scoring of snake length
def home_base(gameWindow, color, snake_size):
    homebase_x = 450
    homebase_y = 300
    color = orange
    pygame.draw.rect(gameWindow, color, [homebase_x, homebase_y, snake_size, snake_size])

#def home_base(gameWindow, color, snk_list, snake_size):
    #homebase_x = 45
    #homebase_y = 55
    #color = orange
    #pygame.draw.rect(gameWindow, color, [homebase_x, homebase_y, snake_size, snake_size])

# GAME LOOP
def gameloop():
    exit_game = False
    game_over = False
    #snake starting placement
    snake_x = 450
    snake_y = 300
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    homebase_x = 45
    homebase_y = 55    

    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(60, screen_height-20)
    score = 0
    init_velocity = 4
    #size of snake square
    snake_size = 10
    fps = 60 # fps = frames per second
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter to Restart", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                #score +=1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height -30)
                snk_length +=5

            if abs(snake_x - homebase_x)<10 and abs (snake_y - homebase_y)<10:
                homebase_storage = []
                for i in homebase_storage:
                    score += 1
                #homebase_storage.extend(snk_length)
                #snk_length = [1]
                #score +=1 (this caused the score to rise as long as snake was at homebase, not what I wanted)

            gameWindow.fill (white)
            text_screen("Score: " + str(score), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, red, (0, 40), (900, 40), 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width - 20 or snake_y<50 or snake_y>screen_height-20:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
            home_base(gameWindow, orange, snake_size)
            #home_base(gameWindow, orange, snake_size, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()
