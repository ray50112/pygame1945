from pathlib import Path
import pygame
from player import Player
from mymissile import MyMissile
from myenemy import Enemy
from myexplosion import Explosion
from mymenu import Menu, GameOver, ScoreBoard
import random

def main():
    parent_path = Path(__file__).parents[0]
    image_path = parent_path / 'res'
    print(image_path)
    icon_path = image_path / 'airplane.png'

    Missiles = []
    Enemys = []
    Booms = []

    pygame.init()

    launchMissile = pygame.USEREVENT + 1
    launchEnemy = pygame.USEREVENT + 2
    screenHigh = 760
    screenWidth = 1000
    playground = [screenWidth, screenHigh]
    screen = pygame.display.set_mode((screenWidth, screenHigh))

    font = pygame.font.SysFont(None, 48)
    font1 = pygame.font.SysFont(None, 24)
    menu = Menu(screen, font)
    menu.run()
    scoreboard = ScoreBoard(screen, font, font1)
    pygame.display.set_caption('Fake 1942')
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
    bg_path = image_path / 'bg.jpg'
    background = pygame.image.load(bg_path).convert() 
    background = pygame.transform.scale(background, (screenWidth, screenHigh))

    running = True
    fps = 120
    clock = pygame.time.Clock()
    movingScale = 600 / fps
    player = Player(playground=playground, sensitivity=movingScale, maxhp = menu._hp)
    keyCountX = 0
    keyCountY = 0
    pygame.time.set_timer(launchEnemy, menu._interval)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False

            if event.type == launchMissile:
                m_x = player.x + 20
                m_y = player.y
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player.x + 80
                Missiles.append(MyMissile(playground, (m_x, m_y), movingScale))

            if event.type == launchEnemy:
                m_x = random.randint(50, screenWidth - 100)
                m_y = -50
                Enemys.append(Enemy(xy=(m_x, m_y), playground=playground, sensitivity=menu._movingScale))

                
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
                    m_x = player.x + 20
                    m_y = player.y
                    Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                    m_x = player.x + 80
                    Missiles.append(MyMissile(playground, (m_x, m_y), movingScale))
                    pygame.time.set_timer(launchMissile, 400)
                if event.key == pygame.K_t:
                    game_over = GameOver(screen, font, menu._selected_mode)
                    game_over.run()
                    return game_over._result  # 重新開始或退出由使用者決定
                
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
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(launchMissile, 0)


        screen.blit(background, (0,0))
        
        player.collision_detect(Enemys)
        for e in Missiles:
            e.collision_detect(Enemys)  
        
        for e in Enemys:
            if e._collided:
                Booms.append(Explosion(e._center))
                scoreboard.add(10)
        
        Missiles = [item for item in Missiles if item._available]
        for m in Missiles:
            m.update()
            screen.blit(m._image, m.xy)
        
        Enemys = [item for item in Enemys if item._available]
        for e in Enemys:
            e.update()
            screen.blit(e._image, e.xy)
        

        player.update()
        screen.blit(player._image, player.xy)
        player.draw_hp_bar(screen)
        if not player._available:
            game_over = GameOver(screen, font, menu._selected_mode)
            game_over.run()
            return game_over._result
                
        Booms = [item for item in Booms if item._available]
        for e in Booms:
            e.update()
            screen.blit(e._image, e.xy)
        scoreboard.draw()
        pygame.display.update()
        dt = clock.tick(fps)

    pygame.quit()


while True:
    restart = main()
    if not restart:
        break