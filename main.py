import pygame
from rocket import Rocket

# print("Hello, World")

pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Teste Janela")


drawGroup = pygame.sprite.Group()
rocket = Rocket(drawGroup)

def draw():
    display.fill([25, 25, 112])


gameloop = True
isPressingW = False

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    draw()
    drawGroup.update()
    drawGroup.draw(display)
    pygame.display.update()