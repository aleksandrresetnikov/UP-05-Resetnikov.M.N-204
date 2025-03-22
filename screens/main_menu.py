from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)

        label = Label(text="Главное меню", font_size=40)
        play_button = Button(text="Играть", font_size=30, on_press=self.start_game)
        market_button = Button(text="Скины", font_size=30, on_press=self.open_market)

        layout.add_widget(label)
        layout.add_widget(play_button)
        layout.add_widget(market_button)
        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = "game"  # Переключение на игру

    def open_market(self, instance):
        self.manager.current = "market"  # Переключение на игру
