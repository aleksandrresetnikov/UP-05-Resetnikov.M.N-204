from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class GameOverScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)

        label = Label(text="Вы проиграли!", font_size=40)
        restart_button = Button(text="Заново", font_size=30, on_press=self.restart_game)
        menu_button = Button(text="В меню", font_size=30, on_press=self.back_to_menu)

        layout.add_widget(label)
        layout.add_widget(restart_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def restart_game(self, instance):
        self.manager.get_screen("game").reset_game()
        self.manager.current = "game"

    def back_to_menu(self, instance):
        self.manager.get_screen("game").reset_game()
        self.manager.current = "main_menu"