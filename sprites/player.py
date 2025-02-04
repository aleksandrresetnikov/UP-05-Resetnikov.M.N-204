from kivy.uix.image import Image
from kivy.clock import Clock

class Player(Image):
    def __init__(self, source, **kwargs):
        super().__init__(source=source, **kwargs)
        self.size_hint = (None, None)
        self.width, self.height = 100, 100
        self.x, self.y = 200, 200

        self.step = 5
        self.game = None  # Ссылка на Game, назначается позже

        Clock.schedule_interval(self.update, 1 / 60)  # Обновление 60 раз в секунду

    def set_game(self, game):
        """ Устанавливает ссылку на Game для доступа к keys_pressed """
        self.game = game

    def update(self, dt):
        if self.game:
            keys = self.game.keys_pressed
            if 119 in keys:  # Вверх
                self.y += self.step
            if 115 in keys:  # Вниз
                self.y -= self.step
            if 100 in keys:  # Вправо
                self.x += self.step
            if 97 in keys:  # Влево
                self.x -= self.step