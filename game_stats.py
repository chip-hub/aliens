class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # Рекорд
        try:
            with open('record.dat', 'r') as file_obj:
                best_score = file_obj.read()
        except FileNotFoundError:
            best_score = '0'
        self.high_score = int(best_score)
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1