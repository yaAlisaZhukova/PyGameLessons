import pygame

# Inherit from pygame.sprite.Sprite
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('img/ghost.png')
        self.rect = self.image.get_rect(topleft=(x, y)) # Get the rect and position it

        self.speed = 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 820:
            self.rect.x = -200



