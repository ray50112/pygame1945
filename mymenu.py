import pygame

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self._selected_mode = None
        self._interval = 0
        self._hp = 0
        self._movingScale = 0

    def run(self):
        while self._selected_mode is None:
            self.screen.fill((0, 0, 0))
            title = self.font.render("Fake 1942 - Mode Select", True, (255, 255, 255))
            train = self.font.render("1. Train", True, (255, 255, 0))
            easy = self.font.render("2. Easy", True, (0, 255, 0))
            hard = self.font.render("3. Hard", True, (255, 0, 0))

            # 置中
            center_x = self.screen.get_width() // 2
            self.screen.blit(title, title.get_rect(center=(center_x, 200)))
            self.screen.blit(train, train.get_rect(center=(center_x, 300)))
            self.screen.blit(easy, easy.get_rect(center=(center_x, 350)))
            self.screen.blit(hard, hard.get_rect(center=(center_x, 400)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self._selected_mode = "train"
                        self._interval = 400
                        self._hp = float('inf')  # 血量無限大
                        self._movingScale = 5
                    elif event.key == pygame.K_2:
                        self._selected_mode = "easy"
                        self._interval = 400
                        self._hp = 100
                        self._movingScale = 5
                    elif event.key == pygame.K_3:
                        self._selected_mode = "hard"
                        self._interval = 800
                        self._hp = 10
                        self._movingScale = 10
    
class GameOver:
    def __init__(self, screen, font, mode):
        self.screen = screen
        self.font = font
        self._result = None
        self._mode = mode
        
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            msg = self.font.render("Game Over", True, (255, 0, 0))
            tip1 = self.font.render("Press R to Restart", True, (0, 255, 0))
            tip = self.font.render("Press ESC to Quit", True, (255, 255, 255))
            
            center_x = self.screen.get_width() // 2
            self.screen.blit(msg, msg.get_rect(center=(center_x, 300)))
            self.screen.blit(tip1, tip1.get_rect(center=(center_x, 350)))
            self.screen.blit(tip, tip.get_rect(center=(center_x, 400)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._result = False
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self._result = True
                    return  # 返回呼叫者 → 代表要重新開始
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                    self._result = True
                    return
    
class ScoreBoard:
    def __init__(self, screen, font, smallfont, x=10, y=10, color=(255, 255, 0)):
        self.screen = screen
        self.font = font
        self.smallfont = smallfont
        self._score = 0
        self._x = x
        self._y = y
        self._color = color

    def add(self, points):
        self._score += points

    def reset(self):
        self._score = 0

    def draw(self):
        text = self.font.render(f"Score: {self._score}", True, (255, 255, 0))
        self.screen.blit(text, (self._x, self._y))
        text2 = self.smallfont.render(f"Print t Retry The Mode", True, (0, 255, 0))
        self.screen.blit(text2, (self._x, self._y + 50))