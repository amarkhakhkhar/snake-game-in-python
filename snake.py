import math
import pygame
import random
import time

pygame.init()
snake_speed = 15

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))
width = 800
height = 600
pygame.display.set_caption("Snake Game!")
icon = pygame.image.load('snakeLogo.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


apple = pygame.image.load('apple.png')
apple = pygame.transform.scale(apple, (20, 17))


def isCollision(sX, sY, aX, aY):
    dist = math.sqrt((math.pow(sX-aX, 2))+(math.pow(sY-aY, 2)))
    if(dist < 21):
        return True
    else:
        return False

# font_style = pygame.font.SysFont(bold=True, size=50, name='Arial')


def message(msg, color, font, size, x, y):
    mesg_font = pygame.font.SysFont(font, size)
    mesg_surface = mesg_font.render(msg, True, color)
    mesg_box = mesg_surface.get_rect()
    mesg_box.midtop = (x, y)
    screen.blit(mesg_surface, mesg_box)
    pygame.display.flip()


score1 = 0


def show_score(score, color, font, size):
    score1 = score
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score1), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

# def snake_Add(s,):


running = True
game_over = False


def gameLoop():

    score = score1
    direction = 'RIGHT'
    change_to = direction

    snake_body = [[width/2, height/2]]

    appleX = random.randint(10, width-10)
    appleY = random.randint(10, height-10)
    snake_position = [width/2, height/2]
    # snakeXchange=0
    # snakeYchange=0
    # snakeX=width/2
    # snakeY=height/2

    def appleImg():
        screen.blit(apple, (appleX, appleY))

    running = True
    game_over = False

    while running:
        screen.fill((0, 170, 0))

        for pos in snake_body:
            pygame.draw.rect(screen, black, pygame.Rect(
                pos[0], pos[1], 15, 15))

        # pygame.draw.rect(screen, black, [snake_position[0],snake_position[1], 15, 15])
        appleImg()
        show_score(score, black, 'times new roman', 50)
        pygame.display.update()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # snakeX+=snakeXchange
        # snakeY+=snakeYchange

            # if(event.type==pygame.KEYDOWN):
            #     if(event.key==pygame.K_LEFT):
            #         snakeXchange=-10
            #     elif(event.key==pygame.K_RIGHT):
            #         snakeXchange=10
            #     elif(event.key==pygame.K_UP):
            #         snakeYchange=-10
            #     elif(event.key==pygame.K_DOWN):
            #         snakeYchange=10

            # if(event.type==pygame.KEYUP):
            #     if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN):
            #         snakeXchange=0
            #         snakeYchange=0

        clock.tick(snake_speed)

        if(snake_position[0] >= width or snake_position[0] < 0 or snake_position[1] >= height or snake_position[1] < 0):
            game_over = True

        collision = isCollision(
            snake_position[0], snake_position[1], appleX, appleY)
        snake_body.insert(0, list(snake_position))

        if(collision):
            appleX = random.randint(10, width-10)
            appleY = random.randint(10, height-10)
            score += 10

        else:
            snake_body.pop()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over = True

        i = 0
        while game_over == True:

            show_gameover(score,i)
            i+=1
            pygame.display.update()
  

            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_q):
                        game_over = False
                        running = False
                    elif (event.key == pygame.K_c):
                        gameLoop()
            

        # pygame.display.update()

    screen.fill(black)
    message('Game Over!', red, 'times new roman', 50, width/2, height/2)
    # pygame.display.update()
    time.sleep(2)
    pygame.quit()
def show_gameover(score,i):
    if(i==0):
        screen.fill(black)
        message("You Lost!", red, 'times new roman', 50, width/2, height/3)
        message("Press Q-Quit or C-Play Again", red,
                    'times new roman', 50, width/2, height/2)
        show_score(score, red, 'times new roman', 50)

gameLoop()
