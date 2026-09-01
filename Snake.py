import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

snake_block = 20
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, pos)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])


def render_message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, pos)

def render_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

game_over = False

while not game_over:

  
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

    while not game_close:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

        value = score_font.render("Score: " + str(Length_of_snake - 1), True, WHITE)
        screen.blit(value, [0, 0])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    while game_close and not game_over:
        screen.fill(BLACK)
        mesg = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, RED)
        screen.blit(mesg, [WIDTH // 6, HEIGHT // 3])
        value = score_font.render("Score: " + str(Length_of_snake - 1), True, WHITE)
        screen.blit(value, [0, 0])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_close = False  

pygame.quit()
sys.exit()
