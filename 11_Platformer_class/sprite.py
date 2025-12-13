import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=(x,y))
        self.dy = 0
        self.onPlatform = False

    def draw(self, screen):
        screen.blit(self.image,self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 3

        if not self.onPlatform:
            self.dy += 1

        self.rect.y += self.dy

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=(x, y))

class GoldenKey(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=(x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class WinScreen(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)