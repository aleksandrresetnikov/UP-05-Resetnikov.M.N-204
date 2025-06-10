import requests
from typing import List, Dict, Optional


class ApiClient:
    def __init__(self, base_url: str = "http://194.87.55.155/v2"):
        self.base_url = base_url

    def update_score(self, player_name: str, score: int) -> Dict:
        """Обновляет рекорд игрока"""
        response = requests.post(
            f"{self.base_url}/update_score",
            json={"player": player_name, "score": score}
        )
        return response.json()

    def get_top_scores(self) -> List[Dict]:
        """Получает топ-10 игроков"""
        response = requests.get(f"{self.base_url}/top_scores")
        return response.json().get("top_scores", [])


api_client_instance = ApiClient()