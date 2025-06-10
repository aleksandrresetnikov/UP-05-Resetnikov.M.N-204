from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from screens.screen_base import ScreenBase
from settings_manager import settings_instance


class RatingMenu(ScreenBase):
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

        menu_button = Button(
            text="Меню",
            color=(255, 255, 255),
            on_press=self.back_menu,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.28, 'y': 0.34},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )

        logo = Image(
            source='assets/promo/logo_rating.png',
            keep_ratio=False,
            x=-65,
            y=260
        )

        self.create_decor(layout)

        layout.add_widget(logo)
        layout.add_widget(menu_button)
        return layout

    def create_decor(self, layout):
        self.create_decor_platform(layout, 65, 0)
        self.create_decor_platform(layout, 105, 125)
        self.create_decor_platform(layout, 85, -165)
        self.create_decor_platform(layout, -95, -235)

        player = Image(
            source='assets/player/Default/left.png',
            keep_ratio=False,
            x=105,
            y=160
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

    def back_menu(self, instance):
        self.manager.current = "main_menu"