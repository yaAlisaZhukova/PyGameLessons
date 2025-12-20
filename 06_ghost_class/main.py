import pygame
from ghost import Ghost

# --- Initialization and setup ---
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite class")

ghost = Ghost(0, 400) # Create a ghost instance

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ghost.update() # Update the player's state

    screen.fill((255, 255, 255)) # Fill the background with white
    screen.blit(ghost.image, ghost.rect) # Draw the player on the screen

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
