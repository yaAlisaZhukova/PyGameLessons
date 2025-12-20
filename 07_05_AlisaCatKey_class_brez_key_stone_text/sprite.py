import random
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (70,70))
        self.rect = self.image.get_rect(topleft=(x,y))

    def draw(self, screen):
        screen.blit(self.image,self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 1 

class GoldenKey(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (70, 50))
        self.rect = self.image.get_rect(topleft=((random.randint(50, 750), random.randint(50, 550))))

class Stone(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=((random.randint(0, 750), random.randint(-650, -50))))

    def update(self):
        self.rect.y += 1
        if self.rect.y == 600:
            self.rect.y = -50          

