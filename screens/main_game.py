from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock

from screens.screen_base import ScreenBase
from sprites.enemy import EnemiesCollector
from sprites.platform import PlatformsCollector
from sprites.player import Player
from settings_manager import settings_instance


class GameScreen(ScreenBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys_pressed = set()
        self.skin = settings_instance.get_select_theme()

        self.platforms = None
        self.player_widget = None
        self.background = None
        self.progressLabel = None
        self.update_bus = []
        self.enemies = None

        self.init_components()

        Window.size = (450, 750)
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)

        Clock.schedule_interval(self.update, 1 / 60)

    def init_components(self):
        self.platforms = None
        self.player_widget = None
        self.background = None
        self.progressLabel = None
        self.update_bus = []
        self.enemies = None

        self.clear_widgets()
        layout = self.create_layout()
        self.add_widget(layout)

    def create_layout(self):
        from kivy.uix.floatlayout import FloatLayout
        layout = FloatLayout()

        self.background = Image(source='assets/background/Default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        self.create_platforms(layout)
        self.update_bus.append(self.platforms)

        self.create_enemies(layout)
        self.update_bus.append(self.enemies)

        self.player_widget = Player(skin=self.skin)
        self.player_widget.set_game(self)
        layout.add_widget(self.player_widget)
        self.update_bus.append(self.player_widget)

        self.progressLabel = Label(font_name='assets/font/DoodleJump.ttf', text='0', pos=(0, 300),
                                   color=[0, 0, 0, 1], font_size=40)
        layout.add_widget(self.progressLabel)

        return layout

    def create_enemies(self, layout):
        self.enemies = EnemiesCollector(layout=layout)

    def on_enter(self):
        skin_name = settings_instance.get_select_theme()
        self.background.source=f'assets/background/{skin_name}.png'
        self.background.reload()

    def update(self, dt):
        for item in self.update_bus:
            item.update(dt)

    def create_platforms(self, layout):
        self.platforms = PlatformsCollector(layout=layout, skin=self.skin)

    def move_platforms(self, x, y, score):
        self.platforms.move_all(x, y, score)

    def fetch_score(self, score_value):
        self.progressLabel.text = str(int(score_value))

    def on_key_down(self, instance, key, *args):
        self.keys_pressed.add(key)

    def on_key_up(self, instance, key, *args):
        self.keys_pressed.discard(key)

    def lose_game(self):
        self.manager.current = "game_over"  # Переключение на экран проигрыша

    def reset_game(self):
        self.init_components()  # Перезапуск игры
