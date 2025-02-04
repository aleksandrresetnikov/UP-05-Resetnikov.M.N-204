import random

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

class PlatformsCollector:
    def __init__(self, skin, layout):
        self.platforms = None
        self.create_platforms(skin, layout)

    def create_platforms(self, skin, layout):
        platform_positions = [(200, 50)]
        for index in range(48*4):
            x = random.randint(64, 450 - 64)
            y = random.randint(150, 2400*2)
            platform_positions.append((x, y))

        self.platforms = []
        for (x, y) in platform_positions:
            platform = Platform(skin=skin, variant=1)
            platform.x = x
            platform.y = y
            self.platforms.append(platform)
            layout.add_widget(platform)

    @staticmethod
    def _check_re_crossing(x1, y1, w1, h1, x2, y2, w2, h2):
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 > y2 - h2 and y1 - h1 < y2

    def check_re_crossing(self, x, y, w, h):
        for platform in self.platforms:
            if self._check_re_crossing(platform.x+25, platform.y, platform.width-50,
                                       platform.height, x, y, w, h):
                return True

        return False

    def move_all(self, x, y):
        remove_stack = []
        for platform in self.platforms:
            platform.x += x
            platform.y += y

            if platform.y < -20:
                remove_stack.append(platform)

        for item in remove_stack:
            self.platforms.remove(item)
