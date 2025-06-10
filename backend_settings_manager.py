import json
import os
from typing import List, Dict, Union


class BackendSettingsManager:
    def __init__(self, file_path: str = "highscores.json"):
        # Создаем директорию для хранения данных, если ее нет
        self.data_dir = "game_data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.file_path = os.path.join(self.data_dir, file_path)
        self.default_settings = {
            "scores": [],
        }
        self.settings = self._load_or_create_settings()

    def _load_or_create_settings(self) -> Dict[str, Union[List[Dict[str, Union[str, int]]], int]]:
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

    def _create_default_settings(self) -> Dict[str, Union[List[Dict[str, Union[str, int]]], int]]:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.default_settings, f, indent=4)
        return self.default_settings.copy()

    def _save_settings(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4)

    def get_all_scores(self) -> List[Dict[str, Union[str, int]]]:
        return self.settings["scores"]

    def set_score_for_player(self, player_name: str, new_score: int):
        scores = self.get_all_scores()
        for index in range(len(scores)):
            score = scores[index]
            if score["player"] == player_name:
                if new_score > score["score"]:  # только если новый рекорд выше
                    self.settings["scores"][index]["score"] = new_score
                    self._save_settings()
                return

        # игрок не найден, добавляем новую запись
        self.settings["scores"].append({
            "player": player_name,
            "score": new_score
        })
        self._save_settings()

    def get_score_for_player(self, player_name: str) -> Union[int, None]:
        scores = self.get_all_scores()
        for score in scores:
            if score["player"] == player_name:
                return score["score"]

        return None

    """Возвращает топ-10 игроков, отсортированных по убыванию score"""
    def get_top_scores(self) -> List[Dict[str, Union[str, int]]]:
        scores = self.settings["scores"]
        sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
        return sorted_scores[:10]


backend_settings_instance = BackendSettingsManager()