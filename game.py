from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image

from sprites.platform import PlatformsCollector
from sprites.player import Player

class Game(App):
    def __init__(self, skin, **kwargs):
        super().__init__(**kwargs)
        self.skin = skin
        self.keys_pressed = set()

        self.platforms = None
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

        self.create_platforms(layout)

        self.player_widget = Player(skin=self.skin)
        self.player_widget.set_game(self)
        layout.add_widget(self.player_widget)

        return layout

    def create_platforms(self, layout):
        self.platforms = PlatformsCollector(layout=layout, skin=self.skin)

    def move_platforms(self, x, y):
        self.platforms.move_all(x, y)

    def on_key_down(self, instance, key, *args):
        self.keys_pressed.add(key)

    def on_key_up(self, instance, key, *args):
        self.keys_pressed.discard(key)