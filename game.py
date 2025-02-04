from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image

from sprites.player import Player


class Game(App):
    player_widget = None
    background = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys_pressed = set()

    def build(self):
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        Window.size = (450, 750)

        return self.init_components()

    def init_components(self):
        layout = FloatLayout()

        self.background = Image(source='assets/background/default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        self.player_widget = Player(source='assets/player/default/left.png')
        self.player_widget.set_game(self)
        layout.add_widget(self.player_widget)

        return layout

    def on_key_down(self, instance, key, *args):
        self.keys_pressed.add(key)

    def on_key_up(self, instance, key, *args):
        self.keys_pressed.discard(key)