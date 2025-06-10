import random

from kivy.uix.image import Image


class Enemy(Image):
    def __init__(self, width, height, x, y, enemy_name, may_be_shoot, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.game = None
        self.source = f'assets/enemies/{enemy_name}.png'
        self.may_be_shoot = may_be_shoot

    def set_game(self, game):
        self.game = game

    def update(self, dt):
        pass

    def get_randomizing_height(self):
        return 550


class MoveEnemy(Enemy):
    def __init__(self, width, height, x, y, enemy_name, may_be_shoot, **kwargs):
        super().__init__(width, height, x, y, enemy_name, may_be_shoot, **kwargs)
        self.move_state = True
        self.target_positive = None
        self.target_negative = None

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


class EnemiesCollector:
    def __init__(self, layout):
        self.enemies = None
        self.create_enemies(layout)

    def generate_enemies_positions(self, count=28, x_range=(64, 386), y_range=(150, 1200)):
        positions = []
        for index in range(count):
            x = random.randint(x_range[0], x_range[1])
            y = random.randint(y_range[0], y_range[1])
            positions.append((x, y))

        return positions

    def create_enemies(self, layout):
        self.enemies = []

        # Спавним big_enemy:
        platform_positions = self.generate_enemies_positions(2, (100, 350), (2000, 3500))
        for (x, y) in platform_positions:
            enemy = Enemy(96, 64, x, y, 'big_enemy', True)
            enemy.x = x
            enemy.y = y
            self.add_enemy(enemy, layout)

        platform_positions = self.generate_enemies_positions(1, (100, 350), (3500, 4500))
        for (x, y) in platform_positions:
            enemy = Enemy(96, 64, x, y, 'void_enemy', False)
            enemy.x = x
            enemy.y = y
            self.add_enemy(enemy, layout)

        platform_positions = self.generate_enemies_positions(2, (100, 350), (2500, 5500))
        for (x, y) in platform_positions:
            enemy = MoveEnemy(96, 64, x, y, 'blue_winged/blue_winged_0', False)
            enemy.x = x
            enemy.y = y
            self.add_enemy(enemy, layout)

    def add_enemy(self, enemy, layout):
        self.enemies.append(enemy)
        layout.add_widget(enemy)

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
                self.reset_enemy(enemy, score)

    def reset_enemy(self, enemy, score):
        enemy.x = random.randint(64, 450 - 64)
        rnd_add_x = random.randint(int(enemy.get_randomizing_height() * 0.5),
                                   int(enemy.get_randomizing_height() * 1.5))
        enemy.y += random.randint(1000, 1200 + int(score / 7) + rnd_add_x)

    def update(self, dt):
        for enemy in self.enemies:
            enemy.update(dt)