import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

brez = pygame.transform.scale(pygame.image.load('img/briz.png'),(70, 70))
brezRect = brez.get_rect(topleft=(50, 50))

goldenKey = pygame.transform.scale(pygame.image.load('img/key.png'),(60, 60))
key_rect_list = []

def addKeys(level_key_number):
    for i in range(level_key_number):
        keyRect = goldenKey.get_rect(topleft=(random.randint(0, 800), random.randint(0, 600)))
        key_rect_list.append(keyRect)

level_key_number = 2
addKeys(level_key_number)

WHITE = (255,255,255)
clock = pygame.time.Clock()

def keyPressed():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        brezRect.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        brezRect.x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        brezRect.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        brezRect.y += 1

run = True
while run:
    clock.tick(90)
    keyPressed()
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(brez, brezRect)

    if len(key_rect_list) == 0:
        level_key_number += 5
        addKeys(level_key_number)

    for i in range(len(key_rect_list)):
        screen.blit(goldenKey, key_rect_list[i])
        if brezRect.colliderect(key_rect_list[i]):
            key_rect_list.pop(i)
            break

    pygame.display.update()
pygame.quit()
sys.exit()