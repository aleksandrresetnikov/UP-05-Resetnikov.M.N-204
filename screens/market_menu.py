from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from components.skin_selector import SkinSelector
from screens.screen_base import ScreenBase
from settings_manager import settings_instance

skins_localization = {
    "Default": 'Обычный дудлик',
    "Doodlestein": 'Дудлштейн',
    "Jungle": 'Джунглевый дудлик',
    "Space": 'Космодудлик',
    "Bunny": 'Дудлик кролик',
    "Underwater": 'Подводный дудлик',
    "Snow": 'Снежный дудлик',
    "Soccer": 'Дудлик футболист'
}

skins_prices = {
    "Default": 0,
    "Doodlestein": 155,
    "Jungle": 125,
    "Space": 100,
    "Bunny": 150,
    "Underwater": 225,
    "Snow": 250,
    "Soccer": 125
}


class MarketMenu(ScreenBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = None
        self.left_label = None
        self.coins_label = None
        self.button_buy = None
        self.price_label = None
        self.init_components()

    def init_components(self):
        self.clear_widgets()

        layout = self.create_layout()
        self.add_widget(layout)

    def on_skin_change(self, skin_name, is_unlocked):
        self.left_label.text = skins_localization[skin_name]

        if is_unlocked:
            self.button_buy.text = "Выбрать"
            self.price_label.text = ""
        else:
            self.button_buy.text = "Купить"
            self.update_price_label()

    def create_layout(self):
        layout = FloatLayout()

        self.background = Image(source='assets/background/Default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        logo = Image(
            source='assets/promo/logo_market.png',
            keep_ratio=False,
            x=-65,
            y=260
        )
        layout.add_widget(logo)

        coin_icon = Image(
            source='assets/promo/coin.png',
            keep_ratio=False,
            x=200,
            y=350
        )
        layout.add_widget(coin_icon)

        self.coins_label = Label(
            text="52",
            size_hint=(1.68, 1.935),
            pos_hint={'x': 0, 'y': 0},
            halign='left',
            valign='middle',
            padding_x=20,
            color=(255, 255, 255)
        )
        layout.add_widget(self.coins_label)

        self.bottom_panel = self.create_bottom_panel()
        layout.add_widget(self.bottom_panel)

        self.skin_selector = SkinSelector(skin_change_event=self.on_skin_change)
        self.skin_selector.processing_layout(layout)

        self.update_coins_label()

        button_back = Button(
            size_hint=(0.28, 0.053),
            pos_hint={'left': 0.98, 'y': 0.08},
            background_normal='assets/buttons/button_menu.png',  # Путь к изображению кнопки
            background_down='assets/buttons/button_menu_press.png'  # Путь к изображению нажатой кнопки
        )
        button_back.bind(on_press=self.back_to_menu)  # Привязка метода buy к нажатию кнопки
        layout.add_widget(button_back)

        return layout

    def on_enter(self):
        self.update_coins_label()

        skin_name = settings_instance.get_select_theme()
        self.skin_selector.select_skin_by_name(skin_name)

        skin_name = settings_instance.get_select_theme()
        self.background.source=f'assets/background/{skin_name}.png'
        self.background.reload()

    def update_coins_label(self):
        self.coins_label.text = str(settings_instance.get_coins())

    def update_price_label(self):
        skin_name = self.skin_selector.get_select_skin_name()
        price = skins_prices[skin_name]
        self.price_label.text = str(price)

    def create_bottom_panel(self):
        panel = FloatLayout(size_hint=(1, 0.1), pos_hint={'bottom': 1})

        panel_background = Image(source='assets/background/market_bottom_panel.png', allow_stretch=True, keep_ratio=False)
        panel.add_widget(panel_background)

        self.left_label = Label(
            text="Космодудлик",
            size_hint=(0.38, 0.75),
            pos_hint={'x': 0, 'y': 0},
            halign='left',
            valign='middle',
            padding_x=20,
            color=(255, 255, 255)
        )
        panel.add_widget(self.left_label)

        self.price_label = Label(
            text="1000",
            size_hint=(0.8, 0.75),
            pos_hint={'right': 0.95, 'y': 0},
            halign='right',
            valign='middle',
            padding_x=20,
            color=(255, 255, 255)
        )
        panel.add_widget(self.price_label)

        self.button_buy = Button(
            size_hint=(0.28, 0.53),
            pos_hint={'right': 0.98, 'y': 0.05},
            background_normal='assets/buttons/button_common.png',  # Путь к изображению кнопки
            background_down='assets/buttons/button_common_press.png',  # Путь к изображению нажатой кнопки
            color=(255, 255, 255)
        )
        self.button_buy.bind(on_press=self.buy)  # Привязка метода buy к нажатию кнопки
        panel.add_widget(self.button_buy)

        return panel

    def back_to_menu(self, instance):
        self.manager.current = "main_menu"

    def buy(self, instance):
        skin_name = self.skin_selector.get_select_skin_name()

        is_unlocked = settings_instance.has_unlocked_theme(skin_name)
        if is_unlocked:
            settings_instance.set_select_theme(skin_name)
            self.background.source = f'assets/background/{skin_name}.png'
            return

        price = skins_prices[skin_name]

        if not settings_instance.spend_coins(price):
            return

        settings_instance.add_unlocked_theme(skin_name)
        settings_instance.set_select_theme(skin_name)

        self.button_buy.text = "Выбрать"
        self.price_label.text = ""
        self.background.source = f'assets/background/{skin_name}.png'
        self.update_coins_label()