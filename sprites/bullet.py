from kivy.uix.image import Image
from kivy.core.window import Window


class Bullet(Image):
    def __init__(self, skin, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = 20, 20
        self.x, self.y = 200, -100
        self.source = f'assets/bullet/{skin}.png'
        self.movable_state = True

    def reset(self, x, y):
        self.x, self.y = x, y
        self.movable_state = True

    def _check_re_crossing(self, x1, y1, w1, h1, x2, y2, w2, h2):
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 > y2 - h2 and y1 - h1 < y2

    def check_enemy_re_crossing(self, enemies):
        for enemy in enemies.enemies:
            if enemy.may_be_shoot and self._check_re_crossing(self.x, self.y, self.width, self.height,
                                  enemy.x, enemy.y, enemy.width, enemy.height):
                enemies.reset_enemy(enemy,  7000)
                return True

        return False

    def update(self, enemies, dt):
        if not self.movable_state:
            return

        if self.check_enemy_re_crossing(enemies):
            self.movable_state = False
            self.x, self.y = 200, -100

        self.y += 17
        screen_height = Window.size[1]
        if self.y >screen_height:
            self.movable_state = False
