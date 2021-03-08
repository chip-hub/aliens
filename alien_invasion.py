import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_whidth, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stars = gf.get_stars(ai_settings)
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения снарядов
    bullets = Group()
    # Создание пришельцев.
    aliens = Group()
    gf.creat_fleet(ai_settings, screen, ship, aliens)

        
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stars)

run_game()