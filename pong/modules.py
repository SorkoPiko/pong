import pygame
from random import randint
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0
        
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.velocity = [randint(3,6),randint(-4,4)]
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-4, 4)