class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_whidth = 1200
        self.screen_height = 800
        self.bg_color = (80, 80, 80)
        # Настройки корабля
        self.ship_limit = 3
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 0, 0
        self.bullets_allowed = 3
        # величина снижения флота
        self.fleet_drop_speed = 10
        # темп ускорения игры
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_setting()
        
    def initialize_dynamic_setting(self):
        """Инициализирует настройки, изменяюиеся в ходе игры."""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # флаг направления движения флота
        self.fleet_direction = 1
        self.alien_points = 10
        
    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)