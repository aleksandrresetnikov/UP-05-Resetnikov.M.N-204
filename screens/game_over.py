from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

from screens.screen_base import ScreenBase
from settings_manager import settings_instance


class GameOverScreen(ScreenBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = None
        self.init_components()

    def init_components(self):
        self.clear_widgets()

        layout = self.create_layout()
        self.add_widget(layout)

    def create_layout(self):
        layout = FloatLayout()

        self.background = Image(source='assets/background/Default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        game_over_text = Image(
            source='assets/promo/game_over_text.png',
            keep_ratio=False,
            x=0,
            y=100
        )
        restart_button = Button(
            text="Играть снова", color=(255, 255, 255),
            on_press=self.restart_game,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.28, 'y': 0.28},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )
        menu_button = Button(
            text="В меню", color=(255, 255, 255),
            on_press=self.back_to_menu,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.72, 'y': 0.28},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )

        self.create_decor(layout)

        layout.add_widget(game_over_text)
        layout.add_widget(restart_button)
        layout.add_widget(menu_button)
        return layout

    def create_decor(self, layout):
        enemy = Image(
            source='assets/enemies/big_enemy.png',
            keep_ratio=False,
            x=65,
            y=35
        )
        layout.add_widget(enemy)

        decor_platform = Image(
            source='assets/platforms/Default/pl1.png',
            keep_ratio=False, x=65, y=0
        )

        layout.add_widget(decor_platform)

    def on_enter(self):
        skin_name = settings_instance.get_select_theme()
        self.background.source = f'assets/background/{skin_name}.png'
        self.background.reload()

    def restart_game(self, instance):
        self.manager.get_screen("game").reset_game()
        self.manager.current = "game"

    def back_to_menu(self, instance):
        self.manager.get_screen("game").reset_game()
        self.manager.current = "main_menu"