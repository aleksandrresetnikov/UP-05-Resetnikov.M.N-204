from kivy.uix.image import Image


class CoinItem(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'assets/promo/coin.png'


class JetPackItem(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'assets/bonuses/items/jetpack.png'


class PowerUpItem(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'assets/bonuses/items/power_up.png'
