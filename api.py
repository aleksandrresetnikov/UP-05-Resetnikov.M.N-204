import requests
from typing import List, Dict, Optional


class ApiClient:
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url

    def update_score(self, player_name: str, score: int) -> Dict:
        """Обновляет рекорд игрока (POST /api/update_score)"""
        response = requests.post(
            f"{self.base_url}/api/update_score",
            json={"player": player_name, "score": score}
        )
        return response.json()

    def get_all_scores(self) -> List[Dict]:
        """Получает все рекорды (GET /api/scores)"""
        response = requests.get(f"{self.base_url}/api/scores")
        return response.json().get("scores", [])

    def get_top_scores(self) -> List[Dict]:
        """Получает топ-10 игроков (GET /api/top_scores)"""
        response = requests.get(f"{self.base_url}/api/top_scores")
        return response.json().get("top_scores", [])

    def get_player_score(self, player_name: str) -> Optional[int]:
        """Получает рекорд конкретного игрока"""
        scores = self.get_all_scores()
        for score in scores:
            if score["player"] == player_name:
                return score["score"]
        return None


api_client_instance = ApiClient()