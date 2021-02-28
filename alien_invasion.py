import pygame
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
    # Создание корабля.
    ship = Ship(ai_settings, screen)
        
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)

        gf.update_screen(ai_settings, screen, ship)

run_game()