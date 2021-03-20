import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from button import Button

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_whidth, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание экземпляров статистики и очков игры.
    stats = GameStats(ai_settings)
    score = Scoreboard(ai_settings, screen, stats)

    stars = gf.get_stars(ai_settings)
    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        

        gf.update_screen(ai_settings, screen, stats, score, ship, aliens, bullets, stars, play_button)

run_game()