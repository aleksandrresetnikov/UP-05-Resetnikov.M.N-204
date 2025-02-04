from kivy.uix.image import Image

class Platform(Image):
    def __init__(self, skin, variant, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = 64, 16

        self.step = 5
        self.game = None
        self.source = f'assets/platforms/{skin}/pl{variant}.png'

    def set_game(self, game):
        self.game = game