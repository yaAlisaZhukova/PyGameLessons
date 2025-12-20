import pygame
import sys
import random
from sprite import Player, GoldenKey, Stone

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
showBrez = True
score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')
 
bullet_img = pygame.transform.scale(pygame.image.load('img/bullet_up.png'),(15, 30))

golden_key_img = pygame.transform.scale(pygame.image.load('img/key.png'),(60, 60)) 
stone_img = pygame.image.load('img/stone.png')

golden_key_group = pygame.sprite.Group() 
stone_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

brez_img = pygame.transform.scale(pygame.image.load('img/brez.png'),(70, 70))
brez = Player(100, 100, brez_img)

def show_text(label, x, y):
   font = pygame.font.Font(None, 36)
   text = font.render(label, True, (180, 0, 0))
   screen.blit(text, (x, y))

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
    clock.tick(60)
    screen.fill(WHITE)
    show_text(str(score), 700, 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                brez.fire(bullet_img, bullet_group)
    
    brez.update()
    stone_group.update()
    bullet_group.update()
    
    if showBrez:
        brez.draw(screen) 
    golden_key_group.draw(screen)
    stone_group.draw(screen)
    bullet_group.draw(screen)

    if pygame.sprite.spritecollide(brez, golden_key_group, True):
        score += 1
    pygame.sprite.groupcollide(stone_group, bullet_group, True, True)

    if pygame.sprite.spritecollide(brez, stone_group, False):
        showBrez = False
     
    if len(golden_key_group) == 0:
        level_key_number += 5
        add_keys(level_key_number)  

    pygame.display.update()
pygame.quit()
sys.exit()