import pygame
import sys
import random
from sprite import Shrimp, Cake

# --- Initialization and setup ---
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite class")
clock = pygame.time.Clock()

score = 0
cake_group = pygame.sprite.Group()
shrimp = Shrimp(80, 300)

def show_text(label, x, y):
   font = pygame.font.Font(None, 36)
   text = font.render(label, True, (180, 0, 0))
   screen.blit(text, (x, y))

def add_cake():
    for i in range(2):
        cake = Cake(880, random.randint(50, 550))
        cake_group.add(cake)

add_cake()

running = True
while running:
    screen.fill((255, 255, 255)) # Fill the background with white
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    show_text(str(score), 750, 50)
    shrimp.update()
    cake_group.update()

    if pygame.sprite.spritecollide(shrimp, cake_group, True):
        score += 1
    if len(cake_group) == 0:
        add_cake()

    shrimp.draw(screen)
    cake_group.draw(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
