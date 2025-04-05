from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MarketMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_components()

    def init_components(self):
        self.clear_widgets()
        layout = self.create_layout()
        self.add_widget(layout)

    def create_layout(self):
        # Основной контейнер
        layout = FloatLayout()

        # Фоновое изображение
        self.background = Image(source='assets/background/Default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        # Нижняя панель
        self.bottom_panel = self.create_bottom_panel()
        layout.add_widget(self.bottom_panel)

        button_back = Button(
            size_hint=(0.28, 0.053),
            pos_hint={'left': 0.98, 'y': 0.08},
            background_normal='assets/buttons/button_menu.png',  # Путь к изображению кнопки
            background_down='assets/buttons/button_menu_press.png'  # Путь к изображению нажатой кнопки
        )
        button_back.bind(on_press=self.back_to_menu)  # Привязка метода buy к нажатию кнопки
        layout.add_widget(button_back)

        return layout

    def create_bottom_panel(self):
        # Контейнер для нижней панели
        panel = FloatLayout(size_hint=(1, 0.1), pos_hint={'bottom': 1})

        # Текстура панели
        panel_background = Image(source='assets/background/market_bottom_panel.png', allow_stretch=True, keep_ratio=False)
        panel.add_widget(panel_background)

        # Лейбл в левой части
        left_label = Label(
            text="Космодудлик",
            size_hint=(0.28, 0.75),
            pos_hint={'x': 0, 'y': 0},
            halign='left',
            valign='middle',
            padding_x=20
        )
        panel.add_widget(left_label)

        # Лейбл в правой части
        right_label = Label(
            text="1000",
            size_hint=(0.8, 0.75),
            pos_hint={'right': 0.95, 'y': 0},
            halign='right',
            valign='middle',
            padding_x=20
        )
        panel.add_widget(right_label)

        # Кнопка в виде изображения
        button_buy = Button(
            size_hint=(0.28, 0.53),
            pos_hint={'right': 0.98, 'y': 0.05},
            background_normal='assets/buttons/button_buy.png',  # Путь к изображению кнопки
            background_down='assets/buttons/button_buy_press.png'  # Путь к изображению нажатой кнопки
        )
        button_buy.bind(on_press=self.buy)  # Привязка метода buy к нажатию кнопки
        panel.add_widget(button_buy)

        return panel

    def back_to_menu(self, instance):
        self.manager.current = "main_menu"

    def buy(self, instance):
        # Логика покупки
        print("Кнопка нажата!")