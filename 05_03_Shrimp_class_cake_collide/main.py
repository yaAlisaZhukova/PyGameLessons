import pygame
import sys
from sprite import Shrimp, Cake

# --- Initialization and setup ---
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite class")
clock = pygame.time.Clock()
showCake = True

shrimp = Shrimp(80, 300)
cake = Cake(880, 300)

running = True
while running:
    screen.fill((255, 255, 255)) # Fill the background with white
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    shrimp.update()
    cake.update()

    if pygame.sprite.collide_rect(shrimp, cake):
        showCake = False

    shrimp.draw(screen)

    if showCake:
        cake.draw(screen)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
