from pathlib import Path
import pygame
from gobject import GameObject
import math

class Player(GameObject):
    
    def __init__(self, playground, xy=None, sensitivity=1, maxhp=100):
        GameObject.__init__(self, playground)
        self._moveScale = 0.5 * sensitivity
        __parent_path = Path(__file__).parent
        self.__player_path = __parent_path/ 'res' / 'airforce1.png'
        self._image = pygame.image.load(self.__player_path)
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2
        self._radius = 0.3 * math.hypot(self._image.get_rect().w, self._image.get_rect().h)
        self._max_hp = maxhp
        self._hp = maxhp
        if xy is None:
            self._x = (self._playground[0]-self._image.get_rect().w) / 2
            self._y = 3 * self._playground[1] / 4
        else:
            self._x = xy[0]
            self._y = xy[1]
        self._objectBound = (10, self._playground[0] - (self._image.get_rect().w + 10), 10, self._playground[1] - (self._image.get_rect().h +10))
        
    def update(self):
        GameObject.update(self)
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2
        
    def collision_detect(self, enemies):
        for m in enemies:
            if self.__collided__(m):
                self._hp -= 10
                if self._hp <= 0:
                    self._available = False
                self._collided = True
                m.hp = -1
                m._collided = True
                m._available = False
                
    def draw_hp_bar(self, surface):
        # 血條比例
        hp_ratio = max(self._hp / self._max_hp, 0)
        # 外框
        pygame.draw.rect(surface, (255, 255, 255), (self._x, self._y - 10, self._image.get_width(), 6), 1)
        # 內部紅條
        pygame.draw.rect(surface, (255, 0, 0), (self._x + 1, self._y - 9, (self._image.get_width() - 2) * hp_ratio, 4))
    
    @property
    def xy(self):
        return self.x, self.y
    

