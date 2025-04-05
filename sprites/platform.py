import random
import time

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

    def has_collision(self):
        return True


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


class BreakablePlatform(Platform):
    def __init__(self, skin, **kwargs):
        super().__init__(skin, 3, **kwargs)
        self.skin = skin
        self.animation_step = 0
        self.animation_state = False

        self.update_current_source()
        self.animation_timer = time.time()
        self.on_break = None

    def begin_broking(self, on_break):
        self.animation_state = True
        self.on_break = on_break

    def reset_animation(self):
        self.animation_state = False
        self.animation_step = 0
        self.on_break = None
        self.update_current_source()

    def update(self, dt):
        self.update_animation()

    def update_animation(self):
        if self.animation_state and self.animation_timer < time.time():
            self.animation_step += 1
            self.animation_timer = time.time() + 0.045

            if self.animation_step >= 7:
                if self.on_break is not None:
                    self.on_break(self)

            self.update_offset()
            self.update_current_source()
            self.update_source_size()

    def update_source_size(self):
        match self.animation_step:
            case 0:
                self.width, self.height = 64, 16
            case 1:
                self.width, self.height = 64, 24
            case 2:
                self.width, self.height = 64, 34
            case 3:
                self.width, self.height = 64, 35

    def update_offset(self):
        match self.animation_step:
            case 0:
                self.y -= 0
            case 1:
                self.y -= 9
            case 2:
                self.y -= 21
            case _:
                self.y -= 24

    def update_current_source(self):
        self.source = f'assets/platforms/{self.skin}/pl3_{self.animation_step}.png'
        if self.animation_step > 3:
            self.source = f'assets/platforms/{self.skin}/pl3_{3}.png'

    def has_collision(self):
        return False


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

        platform_positions = self.generate_platform_positions(3, (100, 350), (2000, 3500))
        for (x, y) in platform_positions:
            move_platform = BreakablePlatform(skin=skin)
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
                return platform

        return None

    def move_all(self, x, y, score):
        for platform in self.platforms:
            platform.x += x
            platform.y += y

            if platform.y < -20:
                self.fetch_platform(platform, score)

    def fetch_platform(self, platform, score):
        platform.x = random.randint(64, 450 - 64)
        rnd_add_x = random.randint(int(platform.get_randomizing_height() * 0.5),
                                   int(platform.get_randomizing_height() * 1.5))
        platform.y += random.randint(1000, 1200 + int(score / 7) + rnd_add_x)

    def update(self, dt):
        for platform in self.platforms:
            platform.update(dt)
