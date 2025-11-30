import pygame
import sys
import random
from sprite import Player 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

brez_img = pygame.transform.scale(pygame.image.load('img/briz.png'),(70, 70))
brez = Player(100,100, brez_img)

golden_key = pygame.transform.scale(pygame.image.load('img/key.png'),(60, 60))
key_rect_list = []

def add_keys(level_key_number):
    for i in range(level_key_number):
        keyRect = golden_key.get_rect(topleft=(random.randint(0, 800), random.randint(0, 600)))
        key_rect_list.append(keyRect)

level_key_number = 2
add_keys(level_key_number)

WHITE = (255,255,255)
clock = pygame.time.Clock() 

run = True
while run:
    clock.tick(90)
     
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    brez.draw(screen)
    brez.update()
     
    if len(key_rect_list) == 0:
        level_key_number += 5
        add_keys(level_key_number)

    for i in range(len(key_rect_list)):
        screen.blit(golden_key, key_rect_list[i])
        if brez.rect.colliderect(key_rect_list[i]):
            key_rect_list.pop(i)
            break

    pygame.display.update()
pygame.quit()
sys.exit()