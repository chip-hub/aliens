class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_whidth = 1200
        self.screen_height = 800
        self.bg_color = (80, 80, 80)
        # Настройки корабля
        self.ship_speed_factor = 2
        # Параметры пули
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 0, 0