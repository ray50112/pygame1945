from pathlib import Path
import pygame
from gobject import GameObject
import random
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
        self._objectBound = (0, self._playground[0], -self._image.get_rect().h - 10, self._playground[1])
        self._moveScale = 0.3 * sensitivity
        self.to_the_bottom()
        self._vx = random.choice([-1, 1]) * random.uniform(1.0, 2.0)

    
    def update(self):
        self._x += self._vx
        if self._x < 0 or self._x > self._objectBound[1] - self._image.get_width():
            self._vx *= -1  # 反向
        
        self._y += self._changeY
        if self._y > self._objectBound[3]:
            self._available = False
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2

    def collision_detect(self, enemies):
        for e in enemies:
            if self.__collided__(e):
                self._hp -= 10
                self._collided = True
                self._available = False
                e.hp = -1
                e._collided = True
                e._available = False

    @property
    def xy(self):
        return self.x, self.y