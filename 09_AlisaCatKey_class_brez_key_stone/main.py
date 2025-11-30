import pygame
import sys
import random
from sprite import Player, GoldenKey, Stone

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
showBrez = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

brez_img = pygame.transform.scale(pygame.image.load('img/brez.png'),(70, 70))
brez = Player(100,100, brez_img)

golden_key_img = pygame.transform.scale(pygame.image.load('img/key.png'),(60, 60)) 
stone_img = pygame.image.load('img/stone.png')

golden_key_group = pygame.sprite.Group() 
stone_group = pygame.sprite.Group() 

def add_keys(level_key_number):
    for i in range(level_key_number):
        golden_key = GoldenKey(golden_key_img)
        golden_key_group.add(golden_key)

def add_stone():
    for i in range(2):
        stone = Stone(stone_img)
        stone_group.add(stone)        

level_key_number = 2
add_keys(level_key_number)
add_stone()

WHITE = (255,255,255)
clock = pygame.time.Clock() 

run = True
while run:
    clock.tick(90) 
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    brez.update()
    stone_group.update()
    
    if showBrez:
        brez.draw(screen) 
    golden_key_group.draw(screen)
    stone_group.draw(screen)

    pygame.sprite.spritecollide(brez, golden_key_group, True)

    if pygame.sprite.spritecollide(brez, stone_group, False):
        showBrez = False
     
    if len(golden_key_group) == 0:
        level_key_number += 5
        add_keys(level_key_number)  

    pygame.display.update()
pygame.quit()
sys.exit()