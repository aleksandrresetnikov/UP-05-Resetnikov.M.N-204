import os
from kivy.core.image import Image as CoreImage

class AssetManager:
    ASSET_DIR = "assets"

    @staticmethod
    def get_path(filename):
        return os.path.join(AssetManager.ASSET_DIR, filename)

    @staticmethod
    def load_image(filename):
        return CoreImage(AssetManager.get_path(filename)).texture