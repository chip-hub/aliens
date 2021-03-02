import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        # Переместить корабль вправо.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Переместить кораблю влево.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        # Отменить переместить корабль вправо.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Отменить переместить корабль влево.
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает снаряд, если еще не достигнут максимум"""
    # Создание нового снаряда и включение его в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Обновляет позиции снарядов и уничтожает старые."""
    # Выводятся все снаряды
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    bullets.update()
    # Удаление пуль, вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Обновляет изображение на экране и отображает новый экран."""
    # Перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # Обновление снарядов
    update_bullets(bullets)
    # Перерисовка корабля
    ship.update()
    ship.blitme()
    # Перерисовка пришельца
    aliens.draw(screen)
    
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def creat_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    # Интервал между соседними пришельцами равен ширине одного пришельца.
    alien = Alien(ai_settings, screen)
    available_space_x = ai_settings.screen_whidth - 2 * alien.rect.width
    number_aliens_x = int(available_space_x / (2 * alien.rect.width))
    # Создание первого ряда пришельцев.
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)