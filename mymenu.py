import pygame

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.selected_mode = None
        self.enemy_interval = 0

    def run(self):
        while self.selected_mode is None:
            self.screen.fill((0, 0, 0))
            title = self.font.render("Fake 1942 - Mode Select", True, (255, 255, 255))
            easy = self.font.render("1. Easy", True, (0, 255, 0))
            hard = self.font.render("2. Hard", True, (255, 0, 0))

            # 置中
            center_x = self.screen.get_width() // 2
            self.screen.blit(title, title.get_rect(center=(center_x, 200)))
            self.screen.blit(easy, easy.get_rect(center=(center_x, 300)))
            self.screen.blit(hard, hard.get_rect(center=(center_x, 350)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.selected_mode = "easy"
                        self.enemy_interval = 400
                    elif event.key == pygame.K_2:
                        self.selected_mode = "hard"
                        self.enemy_interval = 800
        return self.selected_mode, self.enemy_interval
    
class GameOver:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            msg = self.font.render("Game Over", True, (255, 0, 0))
            tip = self.font.render("Press ESC to Quit", True, (255, 255, 255))

            center_x = self.screen.get_width() // 2
            self.screen.blit(msg, msg.get_rect(center=(center_x, 300)))
            self.screen.blit(tip, tip.get_rect(center=(center_x, 400)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    pygame.quit()
                    exit()