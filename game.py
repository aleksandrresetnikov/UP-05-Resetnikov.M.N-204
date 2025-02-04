import random

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image

from sprites.platform import Platform
from sprites.player import Player

class Game(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys_pressed = set()

        self.player_widget = None
        self.background = None

    def build(self):
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        Window.size = (450, 750)

        return self.init_components()

    def init_components(self):
        layout = FloatLayout()

        self.background = Image(source='assets/background/default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        self.player_widget = Player(skin='default')
        self.player_widget.set_game(self)
        layout.add_widget(self.player_widget)

        self.create_platforms(layout)

        return layout

    def create_platforms(self, layout):
        platform_positions = [(50, 52), (100, 75), (150, 52)]
        for index in range(15):
            x = random.randint(64, 450-64)
            y = random.randint(150, 600)
            platform_positions.append((x, y))

        platforms = []
        for (x, y) in platform_positions:
            platform = Platform(skin='default', variant=1)
            platform.x = x
            platform.y = y
            platforms.append(platform)
            layout.add_widget(platform)

    def on_key_down(self, instance, key, *args):
        self.keys_pressed.add(key)

    def on_key_up(self, instance, key, *args):
        self.keys_pressed.discard(key)