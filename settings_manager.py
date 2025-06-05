import json
import os
from typing import List, Dict, Union


class SettingsManager:
    def __init__(self, file_path: str = "settings.json"):
        self.file_path = file_path
        self.default_settings = {
            "unlocked_themes": ["Default"],
            "coins": 0,
            "select_theme": "Default"
        }
        self.settings = self._load_or_create_settings()

    def _load_or_create_settings(self) -> Dict[str, Union[List[str], int]]:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    if not all(key in settings for key in self.default_settings):
                        return self._create_default_settings()
                    return settings
            except (json.JSONDecodeError, IOError):
                return self._create_default_settings()
        else:
            return self._create_default_settings()

    def _create_default_settings(self) -> Dict[str, Union[List[str], int]]:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.default_settings, f, indent=4)
        return self.default_settings.copy()

    def _save_settings(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4)


    def get_unlocked_themes(self) -> List[str]:
        return self.settings["unlocked_themes"]

    def add_unlocked_theme(self, theme: str):
        if theme not in self.settings["unlocked_themes"]:
            self.settings["unlocked_themes"].append(theme)
            self._save_settings()

    def has_unlocked_theme(self, theme_name) -> bool:
        return theme_name in self.get_unlocked_themes()

    def remove_unlocked_theme(self, theme: str):
        if theme == "Default":
            return

        if theme in self.settings["unlocked_themes"] and theme != "Default":
            self.settings["unlocked_themes"].remove(theme)
            self._save_settings()


    def get_coins(self) -> int:
        return self.settings["coins"]

    def add_coins(self, amount: int):
        self.settings["coins"] += amount
        self._save_settings()

    def spend_coins(self, amount: int) -> bool:
        if self.settings["coins"] >= amount:
            self.settings["coins"] -= amount
            self._save_settings()
            return True

        return False


    def get_select_theme(self):
        return self.settings["select_theme"]

    def set_select_theme(self, theme_name) -> bool:
        unlocked_themes = self.get_unlocked_themes()
        if not (theme_name in unlocked_themes):
            return False

        self.settings["select_theme"] = theme_name
        self._save_settings()

        return True


    def get_nickname(self):
        return self.settings["nickname"]

    def set_nickname(self, nickname):
        self.settings["nickname"] = nickname


    def reset_to_default(self):
        self.settings = self.default_settings.copy()
        self._save_settings()


settings_instance = SettingsManager()