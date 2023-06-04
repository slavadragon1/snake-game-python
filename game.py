import pygame
import time
import random


pygame.init()

#display properties
dis_width = 720
dis_height = 576
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('SNAKE')

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

#MAIN LOOP

snake_block = 10
snake_speed = 24

 
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, (dis_width/6, dis_height/3))

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(dis, white, radius=snake_block, center=(x[0], x[1])) #SNAKE BODY


def gameLoop():
    game_close = False
    game_over = False

    moving = None

    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0+snake_block, dis_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0+snake_block, dis_height - snake_block) / 10.0) * 10


    while not game_over:

        while game_close:
            dis.fill(white)
            show_message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and moving != pygame.K_RIGHT:
                    x1_change = -snake_block
                    y1_change = 0
                    moving = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and moving != pygame.K_LEFT:
                    x1_change = snake_block
                    y1_change = 0
                    moving = pygame.K_RIGHT
                elif event.key == pygame.K_UP and moving != pygame.K_DOWN:
                    x1_change = 0
                    y1_change = -snake_block
                    moving = pygame.K_UP
                elif event.key == pygame.K_DOWN and moving != pygame.K_UP:
                    x1_change = 0
                    y1_change = snake_block
                    moving = pygame.K_DOWN

        #границы экрана
        if (x1 >= dis_width) or (x1 < 0) or (y1 >= dis_height) or (y1 < 0):
            game_over = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        pygame.draw.circle(dis, red, center=(foodx, foody), radius=snake_block) #FOOD
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del(snake_List[0])

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_List)

        pygame.display.update()

        if foodx in range(int(x1)-snake_block, int(x1)+snake_block) and foody in range(int(y1)-snake_block, int(y1)+snake_block): #EATING FOOD
            foodx = int(round(random.randrange(0+snake_block, dis_width - snake_block) / 10.0) * 10)
            foody = int(round(random.randrange(0+snake_block, dis_height - snake_block) / 10.0) * 10)
            Length_of_snake += 1

        clock.tick(snake_speed) #скорость змейки

    # show_message('YOU LOST!', red) #Сообщение о закрытии игры
    # pygame.display.update()
    # time.sleep(2) #Время перед закрытием программы

    pygame.quit()
    quit()


gameLoop()