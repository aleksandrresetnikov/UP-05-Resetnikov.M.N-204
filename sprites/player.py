from kivy.uix.image import Image
from kivy.core.window import Window


class Player(Image):
    def __init__(self, skin, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = 100, 100
        self.x, self.y = 200, 200
        self.player_score = 0

        self.step = 5
        self.game = None

        self.textures = {
            "left": f"assets/player/{skin}/left.png",
            "right": f"assets/player/{skin}/right.png",
            "shoot": f"assets/player/{skin}/shoot.png",
            "left_jump": f"assets/player/{skin}/left_jump.png",
            "right_jump": f"assets/player/{skin}/right_jump.png",
            "shoot_jump": f"assets/player/{skin}/shoot_jump.png",
        }

        self.source = self.textures["left"]

    def set_game(self, game):
        self.game = game

    def update_y_movable(self, y):
        if y > 0:
            self.fall_offset = 0
            if self.y < Window.size[1] / 2:
                self.y += y
            else:
                self.player_score += y
                self.update_score_label()
                self.game.move_platforms(0, -y, self.player_score)
        elif not self.check_re_crossing_platform():
            self.fall_offset -= y
            if self.y > 10:
                self.y += y
            else:
                self.game.move_platforms(0, -y, self.player_score)

    def update_score_label(self):
        self.game.fetch_score(self.player_score / 5)

    def check_re_crossing_platform(self):
        if self.game.platforms is None:
            return False

        return self.game.platforms.check_re_crossing(self.x+15, self.y + (self.height*0.005) + 5,
                                                     self.width-30, self.height*0.005)

    fall_offset = 0
    force = 3
    def update_jumping(self):
        self.update_y_movable(self.force)

        if self.force > -7.5:
            self.force -= 0.15

        if self.force < -1 and self.check_re_crossing_platform():
            self.force = 8

    def update(self, dt):
        if self.game.manager.current != "game":
            return

        if self.fall_offset > 1500:
            self.fall_offset = 0
            self.game.lose_game()

        self.update_jumping()
        if self.game:
            keys = self.game.keys_pressed
            '''if 119 in keys:
                self.update_y_movable(self.step)
            if 115 in keys:
                self.update_y_movable(-self.step)'''
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
