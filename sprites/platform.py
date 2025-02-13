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

    def get_randomizing_height(self):
        return 0

    def update(self, dt):
        pass


class MovePlatform(Platform):
    def __init__(self, skin, **kwargs):
        super().__init__(skin, 2, **kwargs)
        self.move_state = True
        self.target_positive = None
        self.target_negative = None

    def get_randomizing_height(self):
        return 550

    def update(self, dt):
        if self.target_positive is None or self.target_negative is None:
            self.target_positive = self.x + 100
            self.target_negative = self.x - 100

        if self.move_state:
            self.x += 1
            if self.x > self.target_positive:
                self.move_state = False
        else:
            self.x -= 1
            if self.x < self.target_negative:
                self.move_state = True


class PlatformsCollector:
    def __init__(self, skin, layout):
        self.platforms = None
        self.create_platforms(skin, layout)

    def add_platform(self, platform, layout):
        self.platforms.append(platform)
        layout.add_widget(platform)

    def generate_platform_positions(self, count=28, x_range=(64, 386), y_range=(150, 1200)):
        platform_positions = []
        for index in range(count):
            x = random.randint(x_range[0], x_range[1])
            y = random.randint(y_range[0], y_range[1])
            platform_positions.append((x, y))

        return platform_positions

    def create_platforms(self, skin, layout):
        platform_positions = self.generate_platform_positions()
        platform_positions.append((200, 50))

        self.platforms = []
        for (x, y) in platform_positions:
            platform = Platform(skin=skin, variant=1)
            platform.x = x
            platform.y = y
            self.add_platform(platform, layout)

        platform_positions = self.generate_platform_positions(2, (100, 350), (2000, 3500))
        for (x, y) in platform_positions:
            move_platform = MovePlatform(skin=skin)
            move_platform.x = x
            move_platform.y = y
            self.add_platform(move_platform, layout)

    @staticmethod
    def _check_re_crossing(x1, y1, w1, h1, x2, y2, w2, h2):
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 > y2 - h2 and y1 - h1 < y2

    def check_re_crossing(self, x, y, w, h):
        for platform in self.platforms:
            if self._check_re_crossing(platform.x+25, platform.y, platform.width-50,
                                       platform.height, x, y, w, h):
                return True

        return False

    def move_all(self, x, y, score):
        for platform in self.platforms:
            platform.x += x
            platform.y += y

            if platform.y < -20:
                platform.x = random.randint(64, 450 - 64)
                rnd_add_x = random.randint(int(platform.get_randomizing_height()*0.5), int(platform.get_randomizing_height()*1.5))
                platform.y += random.randint(1000, 1200 + int(score / 7) + rnd_add_x)

    def update(self, dt):
        for platform in self.platforms:
            platform.update(dt)
