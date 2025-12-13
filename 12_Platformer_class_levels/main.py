import pygame
import sys
import random
from sprite import Player, Platform, GoldenKey, WinScreen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

show_win = False
level = 1
MAX_LEVEL = 2

platform_group = pygame.sprite.Group()

brez_img = pygame.transform.scale(pygame.image.load('img/briz.png'),(70, 70))
brez = Player(100,100, brez_img)

win_img = pygame.image.load('img/win.png')
win = WinScreen(0,0, win_img)

golden_key_img = pygame.transform.scale(pygame.image.load('img/key.png'), (70, 70))
golden_key = GoldenKey(290, 120, golden_key_img)

platform_img = pygame.image.load('img/platform.png')
levels = []
level_1 = [
    { 'x': 10, 'y': 550, },
    { 'x': 240, 'y': 450, },
    { 'x': 490, 'y': 350, },
    { 'x': 240, 'y': 180, },
]
level_2 = [
    { 'x': 10, 'y': 550, },
    { 'x': 270, 'y': 450, },
    { 'x': 10, 'y': 300, },
    { 'x': 280, 'y': 180, },
]
levels.append(level_1)
levels.append(level_2)

def create_platforms(level):
    platform_group.empty()
    for platform_position in levels[level-1]:
        platform = Platform(platform_position['x'],platform_position['y'],platform_img)
        platform_group.add(platform)

create_platforms(level)

WHITE = (255,255,255)
clock = pygame.time.Clock() 

run = True
while run:
    clock.tick(60)
     
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                brez.onPlatform = False
                brez.dy = -19

    brez.draw(screen)
    brez.update()

    golden_key.draw(screen)
    platform_group.draw(screen)

    if pygame.sprite.spritecollide(brez, platform_group, False):
        brez.dy = 0
        brez.onPlatform = True
    else:
        brez.onPlatform = False

    if pygame.sprite.collide_rect(brez, golden_key):
        if level < MAX_LEVEL:
           level += 1
           brez.rect.x = 80
           brez.rect.y = 500
           create_platforms(level)
        else: show_win = True

    if show_win:
        win.draw(screen)

    pygame.display.update()
pygame.quit()
sys.exit()