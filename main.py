from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.game_over import GameOverScreen
from screens.main_game import GameScreen
from screens.main_menu import MainMenu


class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="menu"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(GameOverScreen(name="game_over"))
        return sm


if __name__ == '__main__':
    GameApp().run()
