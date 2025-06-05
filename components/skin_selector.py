from kivy.uix.image import Image
from settings_manager import settings_instance

skins_list = ['Default', 'Doodlestein', 'Jungle', 'Space', 'Bunny',
              'Underwater', 'Snow', 'Soccer']


class SkinSelectorItem(Image):
    def __init__(self, skin, item_index, site, x, y, skin_name, skin_selector, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.item_index = item_index
        self.width, self.height = 100, 100
        self.x, self.y = x, y
        self.skin = skin
        self.source = f"assets/player/{skin}/{site}.png"
        self.skin_name = skin_name
        self.skin_selector = skin_selector
        self.select_state = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return self.skin_selector.select_skin(self.item_index)

        return super().on_touch_down(touch)

    def set_select_state(self, state):
        self.select_state = state


class PlatformDesign(Image):
    def __init__(self, item_index, skin_selector, x, y, **kwargs):
        super().__init__(**kwargs)
        self.item_index = item_index
        self.size_hint = (None, None)
        self.width, self.height = 64, 16
        self.skin_selector = skin_selector
        self.source = f'assets/platforms/Default/pl1.png'
        self.x, self.y = x, y
        self.set_select_state(False)

    def set_select_state(self, state):
        if state:
            self.source = f'assets/platforms/Default/pl2.png'
        else:
            self.source = f'assets/platforms/Default/pl1.png'


class SkinSelector:
    def __init__(self, skin_change_event):
        self.select_index = 0
        self.items = []
        self.platforms = []
        self.skins_indexes = {}
        self.init_items()
        self.skin_change_event = skin_change_event
        self.select_skin(0)

    def init_items(self):
        self.append_item(0, "right", 85,  450, "Default")
        self.append_item(1, "left",  275, 475, "Doodlestein")
        self.append_item(2, "right", 215, 390, "Jungle")
        self.append_item(3, "right", 100, 350, "Space")
        self.append_item(4, "left",  250, 320, "Bunny")
        self.append_item(5, "left",  150, 260, "Underwater")
        self.append_item(6, "left",  315, 210, "Snow")
        self.append_item(7, "right", 55,  190, "Soccer")

    def append_item(self, item_index, site, x, y, skin_name):
        self.skins_indexes[skin_name] = item_index

        selector_item = SkinSelectorItem(skins_list[item_index], item_index, site, x, y, skin_name, self)
        self.items.append(selector_item)

        platform_design = PlatformDesign(selector_item.item_index, self,
                                         selector_item.x + 17, selector_item.y + 10)
        self.platforms.append(platform_design)

    def processing_layout(self, layout):
        for selector_item in self.items:
            layout.add_widget(selector_item)

            layout.add_widget(self.platforms[selector_item.item_index])

    def get_select_platform_item(self):
        return self.platforms[self.select_index]

    def get_select_skin_item(self):
        return self.items[self.select_index]

    def get_select_skin_name(self):
        skin_item = self.get_select_skin_item()
        return skin_item.skin_name

    def select_skin_by_name(self, skin_name):
        index = self.skins_indexes[skin_name]
        self.select_skin(index)

    def select_skin(self, index):
        self.get_select_skin_item().set_select_state(False)
        self.get_select_platform_item().set_select_state(False)

        self.select_index = index

        self.get_select_skin_item().set_select_state(True)
        self.get_select_platform_item().set_select_state(True)

        skin_name = self.get_select_skin_item().skin
        self.skin_change_event(skin_name, settings_instance.has_unlocked_theme(skin_name))
        return True