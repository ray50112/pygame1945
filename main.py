import pygame
from pathlib import Path

parent_path = Path(__file__).parents[0]
image_path = parent_path / 'res'
print(image_path)
icon_path = image_path / 'airplane.png'


pygame.init()

screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))

pygame.display.set_caption('1942偽')
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background.fill((50,50,50))


running = True
fps = 120
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    
    screen.blit(background, (0,0))
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()