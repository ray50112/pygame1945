from pathlib import Path
import pygame
from gobject import GameObject
import math

class Enemy(GameObject):
    
    def __init__(self, playground, xy, sensitivity=1):
        GameObject.__init__(self, playground)
        __parent_path = Path(__file__).parents[0]
        self.__missile_path = __parent_path / 'res' / 'enemy.png'
        self._image = pygame.image.load(self.__missile_path)
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2
        self._radius = self._image.get_rect().w / 2
        self._x = xy[0]
        self._y = xy[1]
        self._exploded = False
        __explosion_path = __parent_path / 'res' / 'explosion_small.png'
        self._explosion_image = pygame.image.load(__explosion_path)
        self._objectBound = (0, self._playground[0], -self._image.get_rect().h - 10, self._playground[1])
        self._moveScale = 0.7 * sensitivity
        self.to_the_bottom()

    
    def update(self):
        if self._exploded:
            if pygame.time.get_ticks() - self._explosion_timer > 300:
                self._available = False
            return
        self._y += self._changeY
        if self._y > self._objectBound[3]:
            self._available = False
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2

    def collision_detect(self, enemies):
        for e in enemies:
            if self.__collided__(e):
                self._hp -= 10
                self._collided = True
                self._exploded = True
                e.hp = -1
                e.collided = True
                e.available = False
                self._explosion_timer = pygame.time.get_ticks()
    @property
    def xy(self):
        return self.x, self.y