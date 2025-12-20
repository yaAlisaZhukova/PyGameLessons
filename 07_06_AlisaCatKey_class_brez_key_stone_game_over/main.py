import pygame
import sys
import random
from sprite import Player, GoldenKey, Stone, GameOver

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat')

brez_img = pygame.transform.scale(pygame.image.load('img/brez.png'), (70, 70))
brez = Player(100, 100, brez_img)

game_over_img = pygame.image.load('img/gameOver.png')
game_over = GameOver(0, 0, game_over_img)

showGameOver = False
showBrez = True

golden_key_img = pygame.transform.scale(pygame.image.load('img/key.png'), (60, 60))
kamen_img = pygame.image.load('img/stone.png')

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
        ke = GoldenKey(golden_key_img)
        gk_group.add(ke)
def add_stone():
    for i in range(3):
        st = Stone(kamen_img)
        st_group.add(st)
add_key(num)
add_stone()

WHITE = (255,255,255)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(90)
    brez.update()
    screen.fill(WHITE)
    st_group.update()
    show_text(str(score), 700, 30)

    if len(gk_group) == 0:
        num += 5
        add_key(num)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.sprite.spritecollide(brez, gk_group, True):
        score += 1
    if pygame.sprite.spritecollide(brez, st_group, True):
        showBrez = False
        showGameOver = True

    if showBrez:
        brez.draw(screen)
    gk_group.draw(screen)
    st_group.draw(screen)

    if showGameOver:
        game_over.draw(screen)

    pygame.display.update()
pygame.quit()
sys.exit()