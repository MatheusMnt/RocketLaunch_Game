from typing import Any
import pygame

class Rocket(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("sprites/Rocket.png")
        self.image = pygame.transform.scale(self.image, [50, 250])
        self.rect = pygame.Rect([60, 50, 50, 250])


    def update(self, *args):
        keys = pygame.key.get_pressed() #Array de Bool 

        if keys[pygame.K_a]:
           self.rect.x -= 1
        if keys[pygame.K_d]:
           self.rect.x += 1