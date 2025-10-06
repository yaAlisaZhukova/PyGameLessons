import pygame

# Inherit from pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('img/mirty10.png')
        self.rect = self.image.get_rect(topleft=(x, y)) # Get the rect and position it

        self.speed = 5

    def update(self):
        # Example: Simple movement based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


