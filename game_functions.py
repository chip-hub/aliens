import sys
from time import sleep
from random import randint

import pygame

from bullet import Bullet
from alien import Alien

# ------------------- Обработка событий!!! ----------------------
def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    # Скрывает указатель мыши
    pygame.mouse.set_visible(False)
    # Сброс игровой статистики.
    stats.reset_stats()
    stats.game_active = True
    # Очистка списков пришельцев и снарядов.
    aliens.empty()
    bullets.empty()
    # Создание нового флота и размещение корабля.
    creat_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        # Переместить корабль вправо.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Переместить кораблю влево.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)
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

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)        

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN and not stats.game_active:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

# ----------------- Снаряды!!! -----------------------------

def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает снаряд, если еще не достигнут максимум"""
    # Создание нового снаряда и включение его в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_bullet_allien_collision(ai_settings, screen, ship, aliens, bullets):
    """Обработка коллизий снарядов с пришельцами."""
    # Удаление снарядов и пришельцев при попадании
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Уничтожение снарядов и создание нового флота
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Обновляет позиции снарядов и уничтожает старые."""
    # Выводятся все снаряды
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    bullets.update()
    # Удаление пуль, вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_allien_collision(ai_settings, screen, ship, aliens, bullets)
    
# ----------------- Обновление флота пришельцев --------------------
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Обрабатывает столкновение корабля с пришельцами."""
    if stats.ships_left > 0:
        # Уменьшение ships_left
        stats.ships_left -= 1

        # Очистка списка пришельцев и пуль.
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Пауза.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Проверяет добрались ли пришельцы до нижнего края экрана."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Проводятся действия те же, что и при столкновении корабря с пришельцами - обновление
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Обновляет позиции всех пришельцев"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

    aliens.update()
    # Проверка коллизий пришельцы-корабль
    if pygame.sprite.spritecollide(ship, aliens, False):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

# ----------------- Обновление экрана!!! ----------------------------

def get_stars(ai_settings):
    stars = []
    max_x = ai_settings.screen_whidth
    max_y = ai_settings.screen_height
    for i in range(100, max_x-100, 150):
        for j in range(100, max_y-200, 150):
            x = randint(-100, 100)
            y = randint(-70, 70)
            stars.append((i+x, j+y))            
    return stars

def draw_stars(screen, stars):
    star = pygame.image.load("images/star.png")
    star_rect = star.get_rect()
    for i in range(len(stars)):
        star_rect.center = stars[i]
        screen.blit(star, star_rect)

def update_screen(ai_settings, stats, screen, ship, aliens, bullets, stars, play_button):
    """Обновляет изображение на экране и отображает новый экран."""
    # Перерисовывается экран.
    screen.fill(ai_settings.bg_color)

    draw_stars(screen, stars)
    

    # Перерисовка корабля
    ship.update()
    ship.blitme()
    # Перерисовка пришельца
    aliens.draw(screen)
    
    # Кнопка Play отображается в том случае, если игра неактивна.
    if not stats.game_active:
        play_button.draw_button()
    else:
        # Обновление снарядов
        update_bullets(ai_settings, screen, ship, aliens, bullets)
        # Обновление флота пришельцев
        update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

# ------------ Пришельцы!!! -------------------
def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов для пришельцев, свободных на экране."""
    available_space_y = (ai_settings.screen_height - 
                        3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    available_space_x = ai_settings.screen_whidth - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien.rect.x = alien.rect.width * (1 + 2 * alien_number)
    alien.rect.y = alien.rect.height * (1 + 2 * row_number)
    aliens.add(alien)

def creat_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                    alien.rect.height)
    # Создание первого ряда пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)