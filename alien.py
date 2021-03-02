import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий пришельца."""
    def __init__(self, ai_settings, screen):
        """Инициализаирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляется в верхнем левом углу.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """Выводит пришельца в текущих координатах."""
        self.screen.blit(self.image, self.rect)