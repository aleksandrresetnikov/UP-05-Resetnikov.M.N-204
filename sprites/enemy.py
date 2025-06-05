import random
import time

from kivy.uix.image import Image


class Enemy(Image):
    def __init__(self, width, height, x, y, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.game = None

    def set_game(self, game):
        self.game = game

    def update(self, dt):
        pass


class EnemiesCollector:
    def __init__(self, layout):
        self.enemies = None
        self.create_enemies(layout)

    def create_enemies(self, layout):
        platform_positions = self.generate_platform_positions(3, (100, 350), (2000, 3500))
        for (x, y) in platform_positions:
            enemy = Enemy()
            enemy.x = x
            enemy.y = y
            self.add_platform(enemy, layout)

    @staticmethod
    def _check_re_crossing(x1, y1, w1, h1, x2, y2, w2, h2):
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 > y2 - h2 and y1 - h1 < y2

    def check_re_crossing(self, x, y, w, h):
        for enemy in self.enemies:
            if self._check_re_crossing(enemy.x+25, enemy.y, enemy.width-50,
                                       enemy.height, x, y, w, h):
                return enemy

        return None

    def move_all(self, x, y, score):
        for enemy in self.enemies:
            enemy.x += x
            enemy.y += y

            if enemy.y < -20:
                self.fetch_enemy(enemy, score)

    def fetch_platform(self, enemy, score):
        enemy.x = random.randint(64, 450 - 64)
        rnd_add_x = random.randint(int(enemy.get_randomizing_height() * 0.5),
                                   int(enemy.get_randomizing_height() * 1.5))
        enemy.y += random.randint(1000, 1200 + int(score / 7) + rnd_add_x)

    def update(self, dt):
        for enemy in self.enemies:
            enemy.update(dt)