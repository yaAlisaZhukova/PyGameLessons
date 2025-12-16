import pygame

class Cake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/cake.png')
        self.rect = self.image.get_rect(topleft=(x, y)) # Get the rect and position it

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= 1

# Inherit from pygame.sprite.Sprite
class Shrimp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/shrimp.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed



