from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.game_over import GameOverScreen
from screens.main_game import GameScreen
from screens.main_menu import MainMenu
from screens.market_menu import MarketMenu


class GameScreenManager(ScreenManager):
    def on_current(self, instance, value):
        current_screen = self.get_screen(value)
        current_screen.on_enter()
        super().on_current(instance, value)


class GameApp(App):
    def build(self):
        sm = GameScreenManager()
        sm.add_widget(MainMenu(name="main_menu"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(GameOverScreen(name="game_over"))
        sm.add_widget(MarketMenu(name="market"))
        return sm


if __name__ == '__main__':
    GameApp().run()
