from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window

class Player(Image):
    def __init__(self, skin, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = 100, 100
        self.x, self.y = 200, 200

        self.step = 5
        self.game = None  # Ссылка на Game, назначается позже

        self.textures = {
            "left": f"assets/player/{skin}/left.png",
            "right": f"assets/player/{skin}/right.png",
            "shoot": f"assets/player/{skin}/shoot.png",
            "left_jump": f"assets/player/{skin}/left_jump.png",
            "right_jump": f"assets/player/{skin}/right_jump.png",
            "shoot_jump": f"assets/player/{skin}/shoot_jump.png",
        }

        self.source = self.textures["left"]

        Clock.schedule_interval(self.update, 1 / 60)  # Обновление 60 раз в секунду

    def set_game(self, game):
        self.game = game

    def update(self, dt):
        if self.game:
            keys = self.game.keys_pressed
            if 100 in keys:
                self.x += self.step
                self.source = self.textures["right"]
                if self.x > Window.size[0] - self.width*0.35:
                    self.x = -self.width*0.35
            if 97 in keys:
                self.x -= self.step
                self.source = self.textures["left"]
                if self.x < -self.width*0.35:
                    self.x = Window.size[0] - self.width*0.35
