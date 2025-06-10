from flask import Flask, request, jsonify

from backend_settings_manager import backend_settings_instance

app = Flask(__name__)

@app.route('/api/update_score', methods=['POST'])
def update_score():
    # Получаем JSON-данные из запроса
    data = request.get_json()

    # Проверяем, что данные корректны
    if not data or 'player' not in data or 'score' not in data:
        return jsonify({"error": "Invalid data. 'player' and 'score' are required."}), 400

    player_name = data['player']
    new_score = data['score']

    # Обновляем рекорд игрока
    backend_settings_instance.set_score_for_player(player_name, new_score)

    return jsonify({"status": "success", "player": player_name, "score": new_score}), 200

@app.route('/api/top_scores', methods=['GET'])
def get_top_scores():
    top_scores = backend_settings_instance.get_top_scores()
    return jsonify({"top_scores": top_scores}), 200

serv_file_path: str = "highscores.json"


if __name__ == '__main__':
    app.run(debug=True)