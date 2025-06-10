from kivy.uix.image import Image


class DashboardPanel(Image):
    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.x, self.y = x, y
        self.source = f"assets/dashboard_panel.png"