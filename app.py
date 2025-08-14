from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/generate-id', methods=['GET', 'POST'])
def generate_id():
    # Генерируем уникальный ID
    unique_id = str(uuid.uuid4())

    # Можно логировать входящие данные от Leadtex, если придут
    incoming_data = request.get_json(silent=True)
    print("Данные от Leadtex:", incoming_data)

    # Отправляем ответ
    return jsonify({
        "SBAID": unique_id
    })

@app.route('/', methods=['GET'])
def home():
    return "Сервер запущен. Endpoint: /generate-id"

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)
