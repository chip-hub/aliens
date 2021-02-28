import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем."""
    def __init__(self, ai_settings, screen, ship):
        """Создает объект снаряда в текущей позиции корабля."""
        super().__init__()
        self.screen = screen
        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        #Обновление позиции прямоугольника.
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        """"Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)