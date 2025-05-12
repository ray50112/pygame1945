from pathlib import Path
import pygame
from player import Player

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
movingScale = 600 / fps
player =Player(playground=playground, sensitivity=movingScale)

keyCountX = 0
keyCountY = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_s:
                keyCountY += 1
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()
            if event.key == pygame.K_SPACE:
                m_x =player.x +20
                m_y = player.y
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if keyCountX == 1:
                    keyCountX = 0
                    player.stop_x()
                else:
                    keyCountX -= 1
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if keyCountY == 1:
                    keyCountY = 0
                    player.stop_y()
                else:
                    keyCountY -= 1
            
    screen.blit(background, (0,0))
    player.update()
    screen.blit(player._image, player.xy)
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()