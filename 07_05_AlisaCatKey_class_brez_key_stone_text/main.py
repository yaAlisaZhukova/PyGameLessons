import pygame
import sys
import random
from sprite import Player, GoldenKey, Stone

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

brez_path = "img/brez.png"
brez = Player(100, 100, brez_path)
showBrez = True
GoldenKey_path = 'img/key.png'
Kamen_path = "img/stone.png"
gk_group = pygame.sprite.Group()
st_group = pygame.sprite.Group()
num = 5
key_rect_list = []
score = 0

def show_text(label, x, y):
   font = pygame.font.Font(None, 36)
   text = font.render(label, True, (180, 0, 0))
   screen.blit(text, (x, y))

def add_key(kluch):
    for i in range(kluch):
        ke = GoldenKey(GoldenKey_path)
        gk_group.add(ke)

def add_stone():
    for i in range(3):
        st = Stone(Kamen_path)
        st_group.add(st)
add_key(num)
add_stone()

WHITE = (255,255,255)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(90)
    screen.fill(WHITE)
    show_text(str(score), 700, 30)
    brez.update()
    st_group.update()
    if len(gk_group) == 0:
        num += 5
        add_key(num)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if showBrez:
        brez.draw(screen)

    if pygame.sprite.spritecollide(brez, gk_group, True):
        score += 1

    if pygame.sprite.spritecollide(brez, st_group, True):
        showBrez = False

    gk_group.draw(screen)
    st_group.draw(screen)
    pygame.display.update()
pygame.quit()
sys.exit()