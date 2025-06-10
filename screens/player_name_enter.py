from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

import settings_manager
from screens.screen_base import ScreenBase
from settings_manager import settings_instance


class PlayerNameScreen(ScreenBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = None
        self.name_input = None
        self.init_components()

    def init_components(self):
        self.clear_widgets()

        layout = self.create_layout()
        self.add_widget(layout)

    def create_layout(self):
        layout = FloatLayout()

        self.background = Image(source='assets/background/Default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        play_button = Button(
            text="Далее",
            color=(255, 255, 255),
            on_press=self.do_continue,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.5, 'y': 0.18},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )

        logo = Image(
            source='assets/promo/logo_main.png',
            keep_ratio=False,
            x=-65,
            y=260
        )

        self.name_input = TextInput(
            text='',
            multiline=False,
            font_size=24,
            hint_text='Введите ваш никнейм',
            size_hint=(0.65, 0.075),
            pos_hint={'center_x': 0.65, 'y': 0.52},
        )
        layout.add_widget(self.name_input)

        self.create_decor(layout)

        layout.add_widget(logo)
        layout.add_widget(play_button)
        return layout

    def create_decor(self, layout):
        self.create_decor_platform(layout, 105-250, 125-100)

        player = Image(
            source='assets/player/Default/left.png',
            keep_ratio=False,
            x=105-250,
            y=160-100
        )
        layout.add_widget(player)

    def create_decor_platform(self, layout, x, y):
        decor_platform = Image(
            source='assets/platforms/Default/pl1.png',
            keep_ratio=False, x=x, y=y
        )

        layout.add_widget(decor_platform)

    def on_enter(self):
        skin_name = settings_instance.get_select_theme()
        self.background.source=f'assets/background/{skin_name}.png'
        self.background.reload()

    def do_continue(self, instance):
        if self.name_input.text == "":
            return

        settings_manager.settings_instance.set_nickname(self.name_input.text)
        self.manager.current = "main_menu"