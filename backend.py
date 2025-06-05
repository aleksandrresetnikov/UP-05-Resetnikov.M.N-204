from flask import Flask, request, jsonify

app = Flask(__name__)

# Обработка GET-запроса (возвращает JSON)
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Это GET-запрос!", "data": [1, 2, 3]})

# Обработка POST-запроса (принимает JSON, возвращает ответ)
@app.route('/api/doodle/login', methods=['POST'])
def post_data():
    data = request.json  # Получаем данные из тела запроса
    print("Получены данные:", data)
    return jsonify({"message": "Данные получены!", "your_data": data})

if __name__ == '__main__':
    app.run(debug=True)  # Запуск сервера (http://127.0.0.1:5000)