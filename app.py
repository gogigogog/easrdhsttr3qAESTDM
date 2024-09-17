from flask import Flask, render_template, request, jsonify
from collections import deque
import os

app = Flask(__name__, static_folder='static', template_folder='templates')


# Очередь для хранения сообщений (не более 100)
messages = deque(maxlen=100)

# Баланс сообщений (пока что будем хранить его локально для демонстрации)
user_balance = {'user_id': {'messages_left': 0}}

@app.route('/')
def balance():
    return render_template('./templates/balance.html')

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    user_id = data.get('userId')

    if user_balance.get(user_id, {}).get('messages_left', 0) > 0:
        if message and user_id:
            # Сохраняем сообщение и уменьшаем баланс сообщений
            messages.append({'text': message, 'userId': user_id})
            user_balance[user_id]['messages_left'] -= 1
        return jsonify({'status': 'Message received'})
    else:
        return jsonify({'status': 'No messages left'})

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(list(messages))

@app.route('/get_balance', methods=['GET'])
def get_balance():
    user_id = request.args.get('userId')
    return jsonify({'messages_left': user_balance.get(user_id, {}).get('messages_left', 0)})

@app.route('/update_balance', methods=['POST'])
def update_balance():
    data = request.get_json()
    user_id = data.get('userId')
    stars = data.get('stars')

    # Предполагается, что функция pop_stars выполнена и вернула количество звезд
    # За каждые 50 звезд дается 1 сообщение
    additional_messages = stars // 50

    if user_id in user_balance:
        user_balance[user_id]['messages_left'] += additional_messages
    else:
        user_balance[user_id] = {'messages_left': additional_messages}

    return jsonify({'messages_left': user_balance[user_id]['messages_left']})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
