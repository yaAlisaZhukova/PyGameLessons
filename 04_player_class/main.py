import pygame
from player import Player

# --- Initialization and setup ---
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player class")

player = Player(screen_width // 2 - 25, screen_height - 200) # Create a player instance

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update() # Update the player's state

    screen.fill((255, 255, 255)) # Fill the background with white
    screen.blit(player.image, player.rect) # Draw the player on the screen

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
