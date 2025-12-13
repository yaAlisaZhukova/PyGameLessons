import pygame
import random

# Inherit from pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (70, 70))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = 3

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def update(self):
        # Example: Simple movement based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

class GoldenKey(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (70, 70))
        self.rect = self.image.get_rect(topleft=(random.randint(0,800), (random.randint(0,600))))


class Kamen(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (70, 70))
        self.rect = self.image.get_rect(topleft=(random.randint(0,800), (random.randint(-600,-50))))

    def update(self):
        self.rect.y += 1
        if self.rect.y == 600:
            self.rect.y = -50