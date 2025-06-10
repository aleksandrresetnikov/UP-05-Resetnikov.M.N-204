from kivy.uix.image import Image
from kivy.uix.label import Label


class DashboardPanel(Image):
    def __init__(self, x, y, data, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width, self.height = 288, 388
        self.x, self.y = x, y
        self.source = f"assets/dashboard_panel.png"
        self.data = data

    def render(self, layout):
        for index in range(len(self.data)):
            item = self.data[index]
            label = Label(
                text=f'#{index + 1}:  {item["player"]}  -  {item["score"]}',
                size_hint=(1.68, 1.935),
                pos_hint={'x': -0.25, 'y': -0.35 - (index * 0.0567)},
                halign='left',
                valign='middle',
                padding_x=20,
                color=(255, 255, 255)
            )

            layout.add_widget(label)
