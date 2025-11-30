import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

brez = pygame.transform.scale(pygame.image.load('img/briz.png'),(70, 70))
brez_rect = brez.get_rect(topleft=(50, 50))

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

def key_pressed():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        brez_rect.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        brez_rect.x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        brez_rect.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        brez_rect.y += 1

run = True
while run:
    clock.tick(90)
    key_pressed()
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(brez, brez_rect)

    if len(key_rect_list) == 0:
        level_key_number += 5
        add_keys(level_key_number)

    for i in range(len(key_rect_list)):
        screen.blit(golden_key, key_rect_list[i])
        if brez_rect.colliderect(key_rect_list[i]):
            key_rect_list.pop(i)
            break

    pygame.display.update()
pygame.quit()
sys.exit()